class Animal:
    def eat(self):
        print("Animal eats")

class Lion(Animal):
    def roar(self):
        print("Lion roars")

class Elephant(Animal):
    def trumpet(self):
        print("Elephant trumpets")
        
def main():
    print("\nHierarchical Inheritance:")
    lion = Lion()
    lion.eat()  # Inherited method from Animal
    lion.roar()  # Lion's own method

    elephant = Elephant()
    elephant.eat()  # Inherited method from Animal
    elephant.trumpet()  # Elephant's own method


if __name__ == "__main__":
    main()
