import asyncio
import time



async def fetch_data(id):
    print(f"Task {id}: Request sent")

    await asyncio.sleep(2)

    print(f"Task {id}: Data recieved")

    return f"Result {id}"


async def main():
    # Schedule multiple coroutines on the Event Loop simultaneously
    results = await asyncio.gather(
        fetch_data(1),
        fetch_data(2)
    )
    print(results)

# Start the Event Loop and run the main coroutine
asyncio.run(main())

