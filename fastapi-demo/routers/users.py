from fastapi import APIRouter, status, HTTPException
from pydantic import BaseModel, Field

# APIRouter groups related endpoints together.
# All routes in this file will start with /users.
router = APIRouter(prefix="/users", tags=["users"])


# Request model: validates incoming JSON when creating a user.
class UserCreate(BaseModel):
    name: str = Field(min_length=2, max_length=100)
    age: int = Field(ge=0, le=150)


# Response model: defines which fields are returned to the client.
class UserResponse(BaseModel):
    id: int
    name: str


# GET /users/{user_id}
# Example: GET /users/10
@router.get("/{user_id}")
def get_user(user_id: int):
    # FastAPI validates that user_id is an integer.
    return {"user_id": user_id}


# POST /users/
# Example JSON body: {"name": "Alice", "age": 25}
@router.post("/")
def create_user(user: UserCreate):
    # FastAPI validates the incoming JSON using UserCreate.
    return {
        "username": user.name,
        "age": user.age,
    }


# POST /users/user_v2/10
# response_model validates and filters the returned response.
@router.post("/user_v2/{user_id}", response_model=UserResponse)
def create_user_v2(user_id: int):
    return {
        "id": user_id,
        "name": "Alice",
        "filtered": "This field will not appear in the response",
    }


@router.get("/status", status_code=status.HTTP_201_CREATED)
def user_status():
    return {"status": "user created"}


@router.get("/http_exception/{user_id}")
def create_user_v3(user_id: int):
    if user_id < 1:
        return HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User ID must be greater than 0",
        )
    return {"user id": user_id}
