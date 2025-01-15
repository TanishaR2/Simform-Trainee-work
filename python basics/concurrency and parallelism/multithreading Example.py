import threading
import time

# Function to calculate square
def calculate_square(number):
    print(f"Calculating square of {number}: {number * number}")
    time.sleep(1)  # Simulate time-consuming task

# Function to calculate cube
def calculate_cube(number):
    print(f"Calculating cube of {number}: {number * number * number}")
    time.sleep(1)  # Simulate time-consuming task

def main():
    # Create two threads
    thread1 = threading.Thread(target=calculate_square, args=(10,))
    thread2 = threading.Thread(target=calculate_cube, args=(10,))
    
    # Start the threads
    thread1.start()
    print("Thread 1 started")
    thread2.start()
    print("Thread 2 started")

    # Wait for both threads to finish
    thread1.join()
    thread2.join()

    print("Both threads have finished.")

if __name__ == "__main__":
    main()
