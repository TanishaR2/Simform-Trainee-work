# Program to demonstrate map() and lambda together

# Example 1: Doubling numbers using map() and lambda
numbers = [1, 2, 3, 4, 5]
doubled_numbers = list(map(lambda x: x * 2, numbers))
print("Doubled numbers:", doubled_numbers)

# Example 2: Squaring numbers using map() and lambda
squared_numbers = list(map(lambda x: x ** 2, numbers))
print("Squared numbers:", squared_numbers)

# Example 3: Converting string list to uppercase using map() and lambda
words = ["apple", "banana", "cherry"]
uppercase_words = list(map(lambda word: word.upper(), words))
print("Uppercase words:", uppercase_words)

# Example 4: Applying a conditional transformation using map() and lambda
# Let's add 10 to the numbers if they are even, else subtract 5 if odd
transformed_numbers = list(map(lambda x: x + 10 if x % 2 == 0 else x - 5, numbers))
print("Transformed numbers (even +10, odd -5):", transformed_numbers)

# Example 5: Using map() with multiple iterables (adding corresponding elements)
# Adding elements from two lists (lists must be of equal length)
list1 = [1, 2, 3, 4]
list2 = [10, 20, 30, 40]
added_lists = list(map(lambda x, y: x + y, list1, list2))
print("Sum of corresponding elements:", added_lists)

# Example 6: Using map() with a function instead of lambda
# Let's define a function to multiply a number by 3 and use map() on it
def multiply_by_three(x):
    return x * 3

multiplied_numbers = list(map(multiply_by_three, numbers))
print("Multiplied numbers by 3:", multiplied_numbers)
