def word_to_number(word):
    word_mapper = {
        "zero": "0",
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9"
    }

    number_str = ""
    i = 0

    while i < len(word):
        matched = False
        for w in word_mapper.keys():
            if word[i:i+len(w)] == w:
                number_str += word_mapper[w]
                i += len(w)
                matched = True
                break
        
        if not matched:
            return None
    
    return int(number_str) if number_str else None


def number_to_word(number):
    num_mapper = {
        '0': 'zero', 
        '1': 'one', 
        '2': 'two', 
        '3': 'three', 
        '4': 'four', 
        '5': 'five', 
        '6': 'six', 
        '7': 'seven', 
        '8': 'eight', 
        '9': 'nine'
    }
    return ''.join(num_mapper[digit] for digit in str(number))


def gcd(a, b):
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a


try:
    input1 = input("Enter the first number (in words): ").strip().lower()
    input2 = input("Enter the second number (in words): ").strip().lower()

    num1 = word_to_number(input1)
    num2 = word_to_number(input2)

    if num1 is None or num2 is None:
        print("Invalid input. Please use words from 'zero' to 'nine'.")
    else:
        result = gcd(num1, num2)
        output = number_to_word(result)
        print(f"GCD (in words): {output}")
except Exception as e:
    print(f"An error occurred: {e}")
