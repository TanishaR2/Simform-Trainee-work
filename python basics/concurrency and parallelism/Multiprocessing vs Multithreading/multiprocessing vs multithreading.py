import threading
import multiprocessing
import time

# Function to calculate the sum of squares of numbers (CPU-bound task)
def calculate_squares(start, end):
    result = 0
    for i in range(start, end):
        result += i * i
    return result

# Multithreading version
def thread_task(start, end):
    thread_result = calculate_squares(start, end)

# Multiprocessing version
def process_task(start, end):
    process_result = calculate_squares(start, end)

def compare_speed():
    num_range = 10**7  # 10 million numbers
    num_threads = 4
    chunk_size = num_range // num_threads

    # Measure time for multithreading
    start_time = time.time()
    threads = []
    for i in range(num_threads):
        start = i * chunk_size
        end = (i + 1) * chunk_size if i < num_threads - 1 else num_range
        thread = threading.Thread(target=thread_task, args=(start, end))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()
    
    threading_time = time.time() - start_time
    print(f"Multithreading Time: {threading_time:.4f} seconds")

    # Measure time for multiprocessing
    start_time = time.time()
    processes = []
    for i in range(num_threads):
        start = i * chunk_size
        end = (i + 1) * chunk_size if i < num_threads - 1 else num_range
        process = multiprocessing.Process(target=process_task, args=(start, end))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()
    
    multiprocessing_time = time.time() - start_time
    print(f"Multiprocessing Time: {multiprocessing_time:.4f} seconds")

if __name__ == "__main__":
    compare_speed()
