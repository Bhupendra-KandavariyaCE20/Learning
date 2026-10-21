import multiprocessing
import time


def heavy_math(name):
    print(f"Process {name} starting...")
    # This locks up the CPU. A thread would block others here, but a Process won't.
    result = sum(i * i for i in range(20_000_000))
    print(f"Process {name} finished!")
    return result

if __name__ == "__main__":
    # Creating two totally separate Python processes
    
    p1 = multiprocessing.Process(target=heavy_math, args=('A',))
    p2 = multiprocessing.Process(target=heavy_math, args=('B',))

    start = time.time()
    p1.start()
    p2.start()

    p1.join()
    p2.join()
    print(f"Total time: {time.time() - start:.2f} seconds")
    # Will run nearly 2x faster than a single process on a multi-core machine.

