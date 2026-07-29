import threading
import time

def fetch_data(id):
    print(f"Starting download {id}...")
    time.sleep(2)  # Simulates waiting for a slow network. The GIL is released here!
    print(f"Finished download {id}")

# Creating two threads that share the same memory process
thread1 = threading.Thread(target=fetch_data, args=(1,))
thread2 = threading.Thread(target=fetch_data, args=(2,))

start = time.time()
thread1.start()
thread2.start()

# Wait for both to finish
thread1.join()
thread2.join()
print(f"Total time: {time.time() - start:.2f} seconds") 
# Output: ~2 seconds (Not 4 seconds! They waited simultaneously.)
