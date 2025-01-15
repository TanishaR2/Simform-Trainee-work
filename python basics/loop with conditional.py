# Use for loop with if-else condition inside
numbers = [1, 2, 3, 4, 5]
print("For loop with if-else inside:")
for num in numbers:
    if num % 2 == 0:
        print(f"{num} is even.")
    else:
        print(f"{num} is odd.")
print()

# Use while loop with if-else condition inside
counter = 1
print("While loop with if-else inside:")
while counter <= 5:
    if counter % 2 == 0:
        print(f"{counter} is even.")
    else:
        print(f"{counter} is odd.")
    counter += 1