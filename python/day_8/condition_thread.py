import threading
import time

condition = threading.Condition()
pizza = []


def consumer():
    with condition:
        while not pizza:
            print("No pizza. Going to sleep...")
            condition.wait()
        print(f"Ate: {pizza.pop()}")


def producer():
    time.sleep(2)
    with condition:
        pizza.append("Mozo pizza")
        print("Pizza is ready! Ringing the bell...")
        condition.notify()


threading.Thread(target=consumer).start()
threading.Thread(target=producer).start()
