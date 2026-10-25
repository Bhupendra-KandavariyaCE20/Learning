from pydantic import BaseModel, ConfigDict, Field


# Data that a client sends to create an item.
class ItemCreate(BaseModel):
    name: str = Field(min_length=2, max_length=100)
    price: float = Field(gt=0)
    quantity: int = Field(ge=0)


# Data that a client can send to update an item.
class ItemUpdate(BaseModel):
    name: str | None = Field(default=None, min_length=2, max_length=100)
    price: float | None = Field(default=None, gt=0)
    quantity: int | None = Field(default=None, ge=0)


# Data returned by the API.
class ItemResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str
    price: float
    quantity: int
