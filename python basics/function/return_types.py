# 1. no return type
def greets():
    print("you are welcomed!")

def greet(name="dear"):
    print("Hello ", name)

def age(year):
    return 2025 - year

def get_coordinates():
    return 5, 10


name = input("Enter your name: ")
year = int(input("Enter your birth year: "))

greet(name)
greets()
print(f"you will be {age(year)} years old in 2025")
x, y = get_coordinates()
print("The coordinates are ", x,y)