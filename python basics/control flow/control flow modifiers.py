"""
Problem: Number Categorization

Write a program that processes numbers from 1 to 10 and:

    Skip even numbers (use continue).
    Stop when it encounters the number 7 (use break).
    Do nothing for the number 5 (use pass).
"""

def numbers(start, end):
    for i in range(start, end + 1):
        if i % 2 == 0:
            continue
        elif i == 7:
            break
        elif i == 5:
            pass
        else:
            print(i)
start, end = 1, 10
# start = int(input("Enter starting of the range: "))
# end = int(input("Enter ending of the range: "))
numbers(start, end)