import os
from authlib.integrations.starlette_client import OAuth
from dotenv import load_dotenv
from fastapi import APIRouter, HTTPException, Request
from fastapi.responses import RedirectResponse

load_dotenv()

router = APIRouter(prefix="/auth", tags=["Authentication"])


# Read credentials from the .env file.
GOOGLE_CLIENT_ID = os.getenv("GOOGLE_CLIENT_ID")
GOOGLE_CLIENT_SECRET = os.getenv("GOOGLE_CLIENT_SECRET")

if not GOOGLE_CLIENT_ID or not GOOGLE_CLIENT_SECRET:
    raise RuntimeError("Google OAuth credentials are missing from .env")

oauth = OAuth()
# Configure the Google OAuth client.
oauth.register(
    name="google",
    client_id=GOOGLE_CLIENT_ID,
    client_secret=GOOGLE_CLIENT_SECRET,
    server_metadata_url=(
        "https://accounts.google.com/.well-known/openid-configuration"
    ),
    client_kwargs={
        "scope": "openid email profile",
    },
)


# GET /auth/login
# Redirect the browser to Google's sign-in page.
@router.get("/login")
async def login(request: Request):
    redirect_uri = request.url_for("google_callback")
    return await oauth.google.authorize_redirect(request, redirect_uri)


# GET /auth/callback
# Google redirects here after the user signs in.
@router.get("/callback", name="google_callback")
async def google_callback(request: Request):
    try:
        # Exchange the authorization code for an access token.
        token = await oauth.google.authorize_access_token(request)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

    # Fetch the user's profile information from Google.
    # user_info = await oauth.google.parse_id_token(request, token)

    user_info = token.get("userinfo")

    # Store only the identity fields needed by our application.
    # SessionMiddleware signs the session cookie.
    request.session["user"] = {
        "google_id": user_info["sub"],
        "email": user_info["email"],
        "name": user_info.get("name", ""),
        "picture": user_info.get("picture"),
    }

    # Return to the API documentation after successful login.
    return RedirectResponse(url="/docs", status_code=303)


# GET /auth/logout
@router.get("/logout")
async def google_logout(request: Request):
    # Clear our application's login session.
    request.session.clear()

    return {"message": "Logged out successfully"}
