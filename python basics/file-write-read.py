with open("data.txt", 'w') as file:
    file.write("hello this is new file!")

with open("data.txt", 'r') as file:
    content = file.read()
    print(content)

with open("data.txt", 'w') as file:
    file.write("hello this is new file! \n ")
    file.write("hello this is new file!")
    file.write("hello this is new file! \n")
    file.write("hello this is new file!")
    file.write("hello this is new file!")

with open("data.txt", 'r') as file:
    content = file.read()
    print(content)