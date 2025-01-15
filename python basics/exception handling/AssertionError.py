def check_age(age):
    assert age >= 18, "Age must be 18 or older."
    return f"Age is {age}"

try:
    print(check_age(16))
except AssertionError as e:
    print(f"Error: {e}")
