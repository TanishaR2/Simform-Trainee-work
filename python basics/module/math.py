import math

def built_in_math_functions():
    # min() and max() functions
    x = min(5, 10, 25)
    y = max(5, 10, 25)
    print(f"The minimum value is: {x}")
    print(f"The maximum value is: {y}")

    # abs() function
    num = -7.25
    abs_value = abs(num)
    print(f"The absolute value of {num} is: {abs_value}")

    # pow() function
    power_result = pow(4, 3)  # Equivalent to 4^3
    print(f"4 to the power of 3 is: {power_result}")

def math_module_functions():
    # sqrt() function
    square_root = math.sqrt(64)
    print(f"The square root of 64 is: {square_root}")

    # ceil() and floor() functions
    ceil_value = math.ceil(1.4)
    floor_value = math.floor(1.4)
    print(f"The ceiling of 1.4 is: {ceil_value}")
    print(f"The floor of 1.4 is: {floor_value}")

    # pi constant
    pi_value = math.pi
    print(f"The value of Pi is: {pi_value}")

def main():
    # Built-in Math Functions
    print("Built-in Math Functions:")
    built_in_math_functions()
    
    # Math Module Functions
    print("\nMath Module Functions:")
    math_module_functions()

if __name__ == "__main__":
    main()
