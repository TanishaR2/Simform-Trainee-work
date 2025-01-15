import multiprocessing
import time

def calculate_square(number):
    print(f"Calculating square of {number}: {number * number}")
    time.sleep(1)

def calculate_cube(number):
    print(f"Calculating the cube of {number}: {number * number * number}")
    time.sleep(1)


def main():
    process1 = multiprocessing.Process(target=calculate_square, args=(10, ))
    process2 = multiprocessing.Process(target=calculate_cube, args=(10, ))
    
    process1.start()
    print("process1 started")
    process2.start()
    print("process2 started")

    process1.join()
    process2.join()

    print("Both processes have finished.")


if __name__ == "__main__":
    main()