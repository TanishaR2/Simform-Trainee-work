def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError as e:
        raise ValueError("Cannot divide by zero.") from e

try:
    divide(5, 0)
except ValueError as ve:
    print(f"Error: {ve}")
