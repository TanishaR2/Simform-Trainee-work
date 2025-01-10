import threading
import time

def func(seconds):
    print(f"Sleeping for {seconds} seconds")
    time.sleep(seconds)

#normal code
func(8)
func(6)
func(3)

#multithreading code
t1 = threading.Thread(target=func, args=8)
t2 = threading.Thread(target=func, args=6)
t3 = threading.Thread(target=func, args=3)

t1.start()
t2.start()
t3.start()