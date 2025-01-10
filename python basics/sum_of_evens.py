def sum_of_evens(a, b):
    count = 0
    for i in range(a, b+1):
        if i%2 == 0:
            print(f"{count} '+' {i} '='")
            count += i
            print(count)
    return count

start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))
print(sum_of_evens(start, end))
