from datetime import datetime

def know_time():
    dat= datetime.now().strftime("%H:%M:%S")
    print(f"Time: {dat}")

know_time()