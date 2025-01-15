# a. for loop with range
print("For loop with range:")
for i in range(1, 6):  # Loop through numbers 1 to 5
    print(i)
print()

# b. for loop with a list
print("For loop with list:")
fruits = ['apple', 'banana', 'cherry']
for fruit in fruits:
    print(fruit)
print()

# c. for loop with a string
print("For loop with string:")
name = "Python"
for letter in name:
    print(letter)
print()

# d. while loop
print("While loop example:")
counter = 0
while counter < 3:
    print("Counter:", counter)
    counter += 1
print()

# e. Simulating a do-while loop (Python doesn't have a native do-while loop)
print("Simulating do-while loop:")
counter = 0
while True:
    print("Counter:", counter)
    counter += 1
    if counter >= 3:
        break  # break when the condition is met
print()

