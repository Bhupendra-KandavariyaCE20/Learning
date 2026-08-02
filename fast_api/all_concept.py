from fastapi import FastAPI, status
from pydantic import BaseModel, EmailStr, Field


app = FastAPI()

# Request Body Schema (What the client SENDS)
class UserCreate(BaseModel):
    username: str = Field(..., min_length=3, max_length=20)
    email: EmailStr
    password: str = Field(..., min_length=8)  # Sensitive field!

# Response Model Schema (What the client RECEIVES)
class UserResponse(BaseModel):
    id: int
    username: str
    email: EmailStr
    # Notice: 'password' is omitted here for security!


# ------------------------------------------------------------------
# 2. ENDPOINT
# ------------------------------------------------------------------

@app.post(
    "/orgs/{org_id}/users",             # Path Parameter in URL
    response_model=UserResponse,        # RESPONSE MODEL (Filters outgoing JSON)
    status_code=status.HTTP_201_CREATED
)
def create_org_user(
        org_id: int,
        user_in: UserCreate,
        send_welcome_email: bool = True
):
    db_user_record = {
        "id": 101,
        "username": user_in.username,
        "email": user_in.email,
        "password": "hashed_secret_password_999",  # Saved in DB
        "org_id": org_id
    }

    if send_welcome_email:
        print(f"Sending welcome email to {user_in.email} for Org #{org_id}")

    # FastAPI will automatically pass 'db_user_record' through 'UserResponse'.
    # 'password' and 'org_id' are stripped out before sending HTTP response!
    return db_user_record


