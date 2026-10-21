import asyncio
import time


async def fetch_data(id):
    print(f"Starting download {id}")

    await asyncio.sleep(2)

    print(f"Finish download {id}")

async def main():
    start_time = time.time()

    await asyncio.gather(
            fetch_data(1),
            fetch_data(2),
            fetch_data(3)
            )
    print(f"Total time: {time.time() - start_time:.2f} seconds")

# 4. Start the Event Loop
asyncio.run(main())
