import queue
import threading
import time

# Create a shared Queue for passing data safely
work_queue = queue.Queue()


def producer():
    for item in ["data_1", "data_2", "data_3"]:
        print(f"Producer sending: {item}")
        work_queue.put(item)  # <--- PASSING DATA TO THE QUEUE
        time.sleep(0.1)  # Simulate a brief delay between items

    # Send a "Poison Pill" (None) to tell the consumer it's time to exit
    work_queue.put(None)


def consumer():
    while True:
        item = work_queue.get()  # <--- RECEIVING DATA FROM THE QUEUE

        # Check for shutdown signal
        if item is None:
            work_queue.task_done()
            break  # Exit the infinite loop gracefully

        print(f"Consumer processed: {item}")
        work_queue.task_done()


# --- START THREADS PART ---

# 1. Instantiate Thread objects pointing to target functions
producer_thread = threading.Thread(target=producer)
consumer_thread = threading.Thread(target=consumer)

# 2. Start execution in the background
producer_thread.start()
consumer_thread.start()

# 3. Wait for all items in the queue to be marked as task_done()
work_queue.join()

# 4. Wait for both threads to completely finish/clean up
producer_thread.join()
consumer_thread.join()

print("All tasks completed successfully!")
