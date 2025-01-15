class NegativeNumberError(Exception):
    pass

def check_positive(num):
    if num < 0:
        raise NegativeNumberError("Negative numbers are not allowed.")
    return num

try:
    num = check_positive(-5)
except NegativeNumberError as e:
    print(f"Custom Exception: {e}")
