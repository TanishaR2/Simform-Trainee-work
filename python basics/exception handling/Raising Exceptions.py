def check_positive_number(num):
    if num < 0:
        raise ValueError("The number cannot be negative.")
    else:
        return num

try:
    result = check_positive_number(-10)
except ValueError as ve:
    print(f"Error: {ve}")
