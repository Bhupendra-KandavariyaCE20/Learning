# main.py

from fastapi import FastAPI
from routers import users, products, sync_async

# Create the main FastAPI application.
app = FastAPI(title="My First FastAPI")


# Register the routers.
# FastAPI combines each router's prefix with its endpoint paths.
app.include_router(users.router)
app.include_router(products.router)
app.include_router(sync_async.router)


# GET /
# Basic home endpoint.
@app.get("/")
def home():
    return {"message": "Hello, FastAPI!"}


# GET /add?a=10&b=20
# a and b are query parameters.
@app.get("/add")
def add(a: int, b: int):
    return {"total": a + b}
