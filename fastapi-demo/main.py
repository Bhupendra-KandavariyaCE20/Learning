from typing import Annotated

from fastapi import Depends, FastAPI
from pydantic import BaseModel

from routers import users, products, sync_async

# Create the FastAPI application.
app = FastAPI(title="My First FastAPI")

# Register routers.
app.include_router(users.router)
app.include_router(products.router)
app.include_router(sync_async.router)


# Define the structure of a user.
class User(BaseModel):
    id: int
    name: str


# Dependency function: provides the current user's information.
# This is mock data, not real authentication.
def get_current_user() -> User:
    return User(id=1, name="Bhup")


# Create a reusable dependency type.
# Any endpoint using CurrentUser receives the dependency result.
CurrentUser = Annotated[User, Depends(get_current_user)]


@app.get("/")
def home():
    return {"message": "Hello, FastAPI!"}


@app.get("/add")
def add(a: int, b: int):
    # FastAPI validates a and b as integers.
    return {"total": a + b}


@app.get("/profile", response_model=User)
def profile(user: CurrentUser):
    # FastAPI injects the result of get_current_user().
    return user
