# Create a set
my_set = {10, 20, 30, 40, 50}

# 1. Accessing Set Items (Sets are unordered, so you can't access them by index, but you can loop through)
print("Accessing Set Items:")
for item in my_set:
    print(item)  # Loop through the set and print each item
print()

# 2. Adding Set Items
print("Adding Set Items:")
my_set.add(60)  # Add a single item to the set
my_set.update([70, 80])  # Add multiple items to the set
print("Set after adding items:", my_set)
print()

# 3. Removing Set Items
print("Removing Set Items:")
my_set.remove(20)  # Remove an item (raises KeyError if item doesn't exist)
# my_set.remove(100)  # Uncommenting this would raise an error because 100 is not in the set
my_set.discard(30)  # Discard an item (doesn't raise an error if item is not found)
removed_item = my_set.pop()  # Remove and return an arbitrary item
print("Set after removals:", my_set)
print("Removed item:", removed_item)
print()

# 4. Looping Through Set Items
print("Looping through Set Items:")
for item in my_set:
    print(item)
print()

# 5. Joining Sets (Sets can be combined using union)
print("Joining Sets:")
set1 = {1, 2, 3}
set2 = {4, 5, 6}
joined_set = set1.union(set2)  # Join two sets
print("Joined set:", joined_set)
print()

# 6. Set Methods
print("Using Set Methods:")
my_set = {10, 20, 30, 40, 50}
print("Length of the set:", len(my_set))  # Length of the set
print("Checking if 20 is in the set:", 20 in my_set)  # Check membership
print("Set after clearing:", my_set.clear())  # Clear all items from the set
print("Set after clearing:", my_set)
