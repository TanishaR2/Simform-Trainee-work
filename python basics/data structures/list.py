# Create a list
my_list = [10, 20, 30, 40, 50]

# 1. Access List Items
print("Accessing List Items:")
print("First item:", my_list[0])  # Access first item
print("Last item:", my_list[-1])  # Access last item
print()

# 2. Change List Items
print("Changing List Items:")
my_list[1] = 25  # Change the second item
print("Updated list:", my_list)
print()

# 3. Add List Items
print("Adding List Items:")
my_list.append(60)  # Add item to the end
my_list.insert(2, 15)  # Insert at index 2
my_list.extend([70, 80])  # Add multiple items at the end
print("List after additions:", my_list)
print()

# 4. Remove List Items
print("Removing List Items:")
my_list.remove(25)  # Remove the item with value 25
my_list.pop(3)  # Remove item at index 3
my_list.clear()  # Clear the entire list
print("List after removals:", my_list)
print()

# 5. Loop Lists
my_list = [10, 20, 30, 40, 50]
print("Looping through List Items:")
for item in my_list:
    print(item)
print()

# 6. List Comprehension
print("List Comprehension:")
squared_list = [x ** 2 for x in my_list]  # Square each item
print("Squared list:", squared_list)
print()

# 7. Sort Lists
print("Sorting List:")
my_list.sort()  # Sort in ascending order
print("Sorted list:", my_list)
my_list.sort(reverse=True)  # Sort in descending order
print("Sorted in descending order:", my_list)
print()

# 8. Copy Lists
print("Copying Lists:")
copied_list = my_list.copy()  # Create a shallow copy
print("Original list:", my_list)
print("Copied list:", copied_list)
print()

# 9. Join Lists (with string elements)
print("Joining Lists:")
string_list = ['Hello', 'world', 'Python']
joined_string = ' '.join(string_list)  # Join with a space
print("Joined string:", joined_string)
print()

# 10. List Methods
print("Using List Methods:")
my_list = [10, 20, 30, 20, 40, 20]
print("Count of 20:", my_list.count(20))  # Count occurrences of 20
print("Index of 40:", my_list.index(40))  # Find index of 40
my_list.reverse()  # Reverse the list
print("Reversed list:", my_list)
