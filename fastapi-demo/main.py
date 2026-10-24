import os
from typing import Annotated

from dotenv import load_dotenv
from fastapi import Depends, FastAPI, HTTPException, Request
from pydantic import BaseModel
from starlette.middleware.sessions import SessionMiddleware

from routers import users, products, sync_async, auth

load_dotenv()

app = FastAPI(title="My First FastAPI")

# SessionMiddleware must be enabled for request.session to work.
session_secret = os.getenv("SESSION_SECRET")
if not session_secret:
    raise RuntimeError("SESSION_SECRET is missing from .env")

app.add_middleware(
    SessionMiddleware,
    secret_key=session_secret,
    same_site="lax",
    https_only=False,  # Local HTTP development only!
    session_cookie="fastapi_session",
)

# Register your existing routers and the new auth router.
app.include_router(users.router)
app.include_router(products.router)
app.include_router(sync_async.router)
app.include_router(auth.router)


# Describe the user information returned by our API.
class User(BaseModel):
    google_id: str
    email: str
    name: str
    picture: str | None = None


# Dependency: retrieve the authenticated user from the session.
def get_current_user(request: Request) -> User:
    user = request.session.get("user")

    # Reject requests that haven't completed Google login.
    if not user:
        raise HTTPException(
            status_code=401,
            detail="Please sign in with Google first",
        )

    return User(**user)


# Reusable dependency type.
CurrentUser = Annotated[User, Depends(get_current_user)]


@app.get("/")
def home():
    return {"message": "Hello, FastAPI!"}


@app.get("/add")
def add(a: int, b: int):
    return {"total": a + b}


@app.get("/health")
def health_check():
    return {"status": "ok"}


# This endpoint now requires a Google login.
@app.get("/profile", response_model=User)
def profile(user: CurrentUser):
    return user
