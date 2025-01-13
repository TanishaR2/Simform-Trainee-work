

# 1. Introduction to List Comprehension
# Basic list comprehension to square numbers
square_numbers = [x**2 for x in range(10)]
print("1. Squares of numbers:", square_numbers)

# 2. List Comprehension with a Single `for` Loop
# Generating a list of even numbers
even_numbers = [x for x in range(20) if x % 2 == 0]
print("2. Even numbers:", even_numbers)

# 3. Conditional List Comprehension
# List comprehension with only even numbers greater than 10
even_above10 = [x for x in range(20) if x % 2 == 0 and x > 10]
print("3. Even numbers above 10:", even_above10)

# 4. List Comprehension with Multiple `for` Loops
# Cartesian product (pairs of numbers from two lists)
pairs = [(x, y) for x in range(2) for y in range(2)]
print("4. Cartesian product (pairs):", pairs)

# 5. List Comprehension with `if-else` Condition
# Assigning 0 if the number is less than 5, else assigning the number
conditional =  [x for x in range(10) if x>=5]
print("5. Numbers with condition (>=5):", conditional)