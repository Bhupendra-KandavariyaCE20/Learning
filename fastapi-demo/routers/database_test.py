from typing import Annotated

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from database import get_db
from sqlalchemy import text

router = APIRouter(prefix="/database", tags=["Database Learning"])

DbSession = Annotated[AsyncSession, Depends(get_db)]


@router.get("/test")
async def test_database(db: DbSession):
    result = await db.execute(text("SELECT 1 AS result"))
    value = result.scalar_one()
    return {"connected": True, "result": value}
