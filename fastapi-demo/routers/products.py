from fastapi import APIRouter
from pydantic import BaseModel, Field

# Every route in this router gets the /products prefix.
router = APIRouter(prefix="/products", tags=["products"])


# Request model with validation rules.
class ProductCreate(BaseModel):
    name: str = Field(min_length=2, max_length=100)

    # Price must be greater than zero.
    price: int = Field(gt=0)

    # Quantity can be zero, but cannot be negative.
    quantity: int = Field(ge=0)


# GET /products/?category=electronics&units=5
# category and units are query parameters because they are
# function parameters that are not path parameters or body models.
@router.get("/")
def get_products(category: str, units: int):
    return {
        "category": category,
        "units": units,
    }


# POST /products/
# Example JSON body:
# {
#     "name": "Keyboard",
#     "price": 1500,
#     "quantity": 10
# }
@router.post("/")
def create_product(product: ProductCreate):
    # Pydantic validates the JSON automatically.
    # model_dump() converts the model to a regular dictionary.
    return product.model_dump()
