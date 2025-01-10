def count_vowels(a):
    count = 0
    str = a
    for i in str:
        if i == 'a' or i =='e' or i == 'i' or i == 'o':
            count += 1

    return count
a = input("Enter string: ")

print(count_vowels(a))
