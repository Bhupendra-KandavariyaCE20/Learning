# routers/sync_async.py

import asyncio
import time

from fastapi import APIRouter

router = APIRouter(
    prefix="/sync_async",
    tags=["Sync and Async Endpoints"],
)


# Simulate a synchronous, blocking operation.
# time.sleep() blocks the thread executing this function.
def slow_database_query() -> int:
    time.sleep(5)
    return 5


# Simulate an asynchronous I/O operation, such as calling an API.
# asyncio.sleep() suspends this coroutine without blocking the event loop.
async def fetch_data_from_api() -> int:
    await asyncio.sleep(3)
    return 3


# GET /sync_async/sync
# FastAPI runs a normal def endpoint in its thread pool.
@router.get("/sync")
def sync_endpoint():
    result = slow_database_query()

    return {
        "endpoint_type": "synchronous",
        "result": result,
        "message": "Simulated blocking operation completed",
    }


# GET /sync_async/async
# FastAPI executes this coroutine on the event loop.
@router.get("/async")
async def async_endpoint():
    # await yields control while the asynchronous operation waits.
    result = await fetch_data_from_api()

    return {
        "endpoint_type": "asynchronous",
        "result": result,
        "message": "Simulated non-blocking operation completed",
    }
