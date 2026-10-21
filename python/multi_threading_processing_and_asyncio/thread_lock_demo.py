import threading

counter = 0
lock = threading.Lock()

def safe_increment(id):
    global counter
    print(f"Thread started {id}")
    for _ in range(1000000):
        with lock:
            counter += 1
    print(f"Thread completed {id}")


t1 = threading.Thread(target=safe_increment, args=(1,))
t2 = threading.Thread(target=safe_increment, args=(2,))



t1.start(); t2.start()
t1.join(); t2.join()

print(f"Final counter: {counter}") # Safely outputs 200,000
