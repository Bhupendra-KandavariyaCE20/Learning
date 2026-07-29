import asyncio
import time
import concurrent.futures


# A legacy, non-async function that blocks the thread (e.g., heavy math or legacy library)
def blocking_heavy_math():
    print("Starting heavy math...")
    time.sleep(3)
    return 42


async def main():
    loop = asyncio.get_running_loop()

    # Create a background thread pool
    with concurrent.futures.ThreadPoolExecutor() as pool:

        # Offload the blocking function to the Executor, but 'await' it safely!
        result = await loop.run_in_executor(pool, blocking_heavy_math)
        print(f"Math finished with result: {result}")


asyncio.run(main())
