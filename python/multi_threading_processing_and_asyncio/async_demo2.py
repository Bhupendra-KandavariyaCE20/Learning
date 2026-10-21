import asyncio
import time

async def fetch_data(task_id:int, delay:int):
    print(f"Task {task_id}: Started (will take {delay}s)")

    # Yield control to the Event Loop while waiting
    await asyncio.sleep(delay)

    print(f'Finished task {task_id} in {delay} time')

    return f"Result {task_id}"


async def main():
    start_time = time.time()

    # Schedule all 3 tasks concurrently
    results = await asyncio.gather(
        fetch_data(1, 2), # Takes 2s
        fetch_data(2, 3), # Takes 3s
        fetch_data(3, 1)  # Takes 1s
    )

    print(f"All tasks completed in {time.time() - start_time:.2f} seconds")
    print(f"Results: {results}")


# Start the Event Loop
asyncio.run(main())

