def is_palindrome(str1):
    str = str1.replace(" " , "").lower()
    if str == str[::-1]:
        print("the given string is a palindrome")

    else:
        print("The given string is not a palindrome")

str1 = input("enter a string to check palindrome: ")
is_palindrome(str1) #man a plan a canal Panama