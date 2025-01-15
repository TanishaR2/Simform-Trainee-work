# Create a tuple
my_tuple = (10, 20, 30, 40, 50)

# 1. Access Tuples
print("Accessing Tuple Items:")
print("First item:", my_tuple[0])  # Access first item
print("Last item:", my_tuple[-1])  # Access last item
print()

# 2. Update Tuples (through list conversion)
print("Updating Tuple Items:")
my_list = list(my_tuple)
my_list[1] = 25  # Change the second item
my_tuple = tuple(my_list)
print("Updated tuple:", my_tuple)
print()

# 3. Unpack Tuples
print("Unpacking Tuple:")
a, b, c, d, e = my_tuple
print("Unpacked values:", a, b, c, d, e)
print()

# 4. Loop Tuples
print("Looping through Tuple Items:")
for item in my_tuple:
    print(item)
print()

# 5. Join Tuples
print("Joining Tuples:")
tuple1 = (100, 200)
tuple2 = (300, 400)
joined_tuple = tuple1 + tuple2
print("Joined tuple:", joined_tuple)
print()

# 6. Tuple Methods
print("Using Tuple Methods:")
my_tuple = (10, 20, 30, 20, 40, 20)
print("Count of 20:", my_tuple.count(20))  # Count occurrences of 20
print("Index of 40:", my_tuple.index(40))  # Find index of 40
