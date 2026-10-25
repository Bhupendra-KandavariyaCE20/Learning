from typing import Annotated


from fastapi import APIRouter, Depends, HTTPException, Request
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from database import get_db
from models import Item
from schema import ItemCreate, ItemResponse, ItemUpdate

router = APIRouter(prefix="/items", tags=["Items Learning"])


DbSession = Annotated[AsyncSession, Depends(get_db)]


# Create
@router.post("/", response_model=ItemResponse, status_code=201)
async def create_item(data: ItemCreate, db: DbSession):
    # convert pydantic model to dict and then to SQLAlchemy model
    item = Item(**data.model_dump())
    db.add(item)
    await db.commit()
    await db.refresh(item)
    return item


@router.get("/", response_model=list[ItemResponse])
async def get_items(db: DbSession):
    result = await db.execute(select(Item))
    items = result.scalars().all()
    return items


@router.put("/{item_id}", response_model=ItemResponse)
async def update_item(item_id: int, data: ItemUpdate, db: DbSession):
    result = await db.execute(select(Item).where(Item.id == item_id))
    item = result.scalar_one_or_none()
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    for key, value in data.model_dump(exclude_unset=True).items():
        setattr(item, key, value)
    await db.commit()
    await db.refresh(item)
    return item


# Delete
@router.delete("/{item_id}", status_code=204)
async def delete_item(item_id: int, db: DbSession):
    result = await db.execute(select(Item).where(Item.id == item_id))
    item = result.scalar_one_or_none()
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    await db.delete(item)
    await db.commit()
    return None
