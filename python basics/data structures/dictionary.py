# Create a dictionary
my_dict = {
    'name': 'John',
    'age': 30,
    'city': 'New York'
}

# 1. Accessing Items
print("Accessing Items:")
print("Name:", my_dict['name'])  # Access by key
print("Age:", my_dict.get('age'))  # Access using get() method (avoids KeyError)
print()

# 2. Changing Items
print("Changing Items:")
my_dict['age'] = 35  # Change the value of 'age'
my_dict['city'] = 'Los Angeles'  # Change the value of 'city'
print("Updated Dictionary:", my_dict)
print()

# 3. Adding Items
print("Adding Items:")
my_dict['email'] = 'john@example.com'  # Add a new key-value pair
my_dict.update({'phone': '123-456-7890'})  # Add using the update() method
print("Dictionary after adding items:", my_dict)
print()

# 4. Removing Items
print("Removing Items:")
my_dict.pop('phone')  # Remove an item by key
removed_item = my_dict.popitem()  # Remove and return an arbitrary key-value pair
print("Dictionary after removing 'phone' and an arbitrary item:", my_dict)
print("Removed arbitrary item:", removed_item)
print()

# 5. Looping Through Dictionary Items
print("Looping Through Dictionary Items:")
print("Using for loop to access keys and values:")
for key, value in my_dict.items():
    print(key, ":", value)
print()

# 6. Copying Dictionaries
print("Copying Dictionaries:")
copied_dict = my_dict.copy()  # Create a shallow copy of the dictionary
print("Copied Dictionary:", copied_dict)
print()

# 7. Nested Dictionaries
print("Nested Dictionaries:")
nested_dict = {
    'person': {
        'name': 'Alice',
        'age': 28
    },
    'address': {
        'city': 'Chicago',
        'zipcode': '60601'
    }
}
print("Nested Dictionary:", nested_dict)
print("Accessing nested dictionary 'person' name:", nested_dict['person']['name'])
print()

# 8. Dictionary Methods
print("Using Dictionary Methods:")
# Get the list of all keys
keys = my_dict.keys()
print("Keys:", keys)

# Get the list of all values
values = my_dict.values()
print("Values:", values)

# Get the list of all key-value pairs as tuples
items = my_dict.items()
print("Items:", items)

# Check if a key exists
key_exists = 'age' in my_dict
print("Does 'age' exist in dictionary?", key_exists)

# Clear all items from the dictionary
my_dict.clear()
print("Dictionary after clearing all items:", my_dict)
