from fastapi import FastAPI
from enum import Enum

class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


# 1. Initialize the FastAPI app
app = FastAPI()


# 2. Define a "route" using a decorator
@app.get("/")
def read_root():
    # 3. Return a standard Python dictionary (FastAPI converts this to JSON)
    return {"message": "Hello, Ubuntu Developer!"}

@app.get("/users/{user_id}")
def get_user(user_id):
    return {"user_id": user_id}


# type validation
@app.get("/items/{item_id}")
def get_item(item_id:int):
    return {"item_id": item_id, "type": type(item_id).__name__}

@app.get("models/{model_name}")
def get_model(model_name: ModelName):
    if model_name == ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    # Because of the Enum validation, we know model_name is safe and valid
    return {"model_name": model_name, "message": "Standard model selected."}

# Query Parameters
@app.get("/items_query")
def get_item_params(item_id: int = 5, is_available: bool = False):
    return {"item_id": item_id, "Avaibility": is_available}

