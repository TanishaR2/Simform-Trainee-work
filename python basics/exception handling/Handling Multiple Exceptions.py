try:
    num = int(input("Enter a number: "))
    result = 10 / num
except ZeroDivisionError:
    print("You cannot divide by zero.")
except ValueError:
    print("Invalid input, please enter a number.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
else:
    print(f"The result is {result}.")
finally:
    print("This block always runs.")
