strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
anagrams = {}  # Use a regular dictionary

for word in strs:
    key = ''.join(sorted(word))  # Sort the word to create the key
    if key not in anagrams:  # Check if the key is already in the dictionary
        anagrams[key] = []  # Initialize the list if the key is missing
    anagrams[key].append(word)  # Append the word to the list for the key

output = list(anagrams.values())  # Convert the grouped values to a list of lists
print(output)


