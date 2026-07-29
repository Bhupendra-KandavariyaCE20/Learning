import threading

rlock = threading.RLock()

def step_one():
    with rlock:
        print("Step 1 done")
        step_two()  # Calls a function that ALSO needs the lock

def step_two():
    with rlock: # If this were a normal Lock, the thread would freeze here forever!
        print("Step 2 done")

# A single thread can safely run this:
step_one()
