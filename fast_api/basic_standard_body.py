from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()

class CreateUser(BaseModel):
    username: str
    email: str
    age: str


@app.post("/createUser")
def create_user(user: CreateUser):
    return {"Name": user.username, "age": user.age}
