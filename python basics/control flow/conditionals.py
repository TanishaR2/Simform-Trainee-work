# Basic if-else condition
age = 25
if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")
print()

# if-elif-else for multiple conditions
temperature = 30
if temperature > 35:
    print("It's hot outside.")
elif temperature > 25:
    print("It's warm outside.")
else:
    print("It's cool outside.")
print()

# Nested if-else condition
x = 10
if x > 5:
    if x % 2 == 0:
        print(f"{x} is greater than 5 and even.")
    else:
        print(f"{x} is greater than 5 but odd.")
else:
    print(f"{x} is 5 or less.")
print()

# Using logical operators (and, or, not)
is_raining = False
has_umbrella = True
if not is_raining or has_umbrella:
    print("You can go outside.")
else:
    print("You should stay inside.")
print()
