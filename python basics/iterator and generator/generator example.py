def even_numbers(limit):
    num = 0
    while num < limit:
        yield num
        num +=2

evens = even_numbers(20)

for even in evens:
    print(even)
