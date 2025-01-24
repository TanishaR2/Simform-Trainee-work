# 3. Given an array of strings strs, group the anagrams together. You can return the answer in any order.

#     An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

#     Constraints:

#         - 1 <= strs.length <= 104

#         - 0 <= strs[i].length <= 100

#         - strs[i] consists of lowercase English letters.

#     Example 1:

#         - Input: strs = ["eat","tea","tan","ate","nat","bat"]

#         - Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

#     Example 2:

#         - Input: strs = [""]

#         - Output: [[""]]

#     Example 3:

#         - Input: strs = ["a"]

#         - Output: [["a"]]

# l1 = []



# from collections import defaultdict

# strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
# anagrams = {}

# for word in strs:
#     anagrams[''.join(sorted(word))].append(word)

# output = list(anagrams.values())
# print(output)


strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
anagrams = {}  # Use a regular dictionary

for word in strs:
    key = ''.join(sorted(word))  # Sort the word to create the key
    if key not in anagrams:  # Check if the key is already in the dictionary
        anagrams[key] = []  # Initialize the list if the key is missing
    anagrams[key].append(word)  # Append the word to the list for the key

output = list(anagrams.values())  # Convert the grouped values to a list of lists
print(output)


