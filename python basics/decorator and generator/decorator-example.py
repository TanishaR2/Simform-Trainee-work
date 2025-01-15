def decorator(func):
    def wrapper():
        print("Before calling the function")
        func()
        print("Before calling the function")
    return wrapper


@decorator
def greet():
    print("Hello, How are you?")

greet()
