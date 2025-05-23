def func_without_parameters():
    print("Hello, How are you?")

func_without_parameters()

#positional parametres
def pos_params(name, age):
    print(f"{name} is {age} years old.")

pos_params('Alice', 25)

#keyword parameters
def keyword_params(name, age):
    print(f"{name} is {age} years old.")

keyword_params(age=25, name='Alice')

#default
def myFunc(name, age=25):
    print(f"{name} is {age} years old.")

myFunc('Alice')
myFunc('Bob')

#variable-length params
def greet(*names):
    for name in names:
        print(f"Hello {name}!")

greet("alice", "bob", "charlie")

def details(**people):
    for name, age in people.items():
        print(f"hello {name}, you are {age} years old.")

details(Alice=25, bob=20, charlie=15)
