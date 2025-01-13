# Single Inheritance
class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

# Multiple Inheritance
class Flyable:
    def fly(self):
        print("Can fly")

class Swimmable:
    def swim(self):
        print("Can swim")

class Duck(Flyable, Swimmable):  # Inheriting from both Flyable and Swimmable
    def quack(self):
        print("Duck quacks")

# Multilevel Inheritance
class Vehicle:
    def move(self):
        print("Vehicle moves")

class Car(Vehicle):
    def drive(self):
        print("Car drives")

class ElectricCar(Car):  # ElectricCar is a subclass of Car, which is a subclass of Vehicle
    def charge(self):
        print("Electric car is charging")

# Hierarchical Inheritance
class Animal:
    def eat(self):
        print("Animal eats")

class Lion(Animal):
    def roar(self):
        print("Lion roars")

class Elephant(Animal):
    def trumpet(self):
        print("Elephant trumpets")

# Hybrid Inheritance (Combination of Multiple & Multilevel Inheritance)
class Printer:
    def print_doc(self):
        print("Printing document")

class Scanner:
    def scan_doc(self):
        print("Scanning document")

class Copier(Printer, Scanner):
    def copy_doc(self):
        print("Copying document")

# Main program to demonstrate all types of inheritance
def main():
    # Demonstrate Single Inheritance
    print("Single Inheritance:")
    dog = Dog()
    dog.speak()  # Inherited method from Animal
    dog.bark()  # Dog's own method

    print("\nMultiple Inheritance:")
    duck = Duck()
    duck.fly()  # Method from Flyable
    duck.swim()  # Method from Swimmable
    duck.quack()  # Duck's own method

    print("\nMultilevel Inheritance:")
    electric_car = ElectricCar()
    electric_car.move()  # Inherited method from Vehicle
    electric_car.drive()  # Inherited method from Car
    electric_car.charge()  # ElectricCar's own method

    print("\nHierarchical Inheritance:")
    lion = Lion()
    lion.eat()  # Inherited method from Animal
    lion.roar()  # Lion's own method

    elephant = Elephant()
    elephant.eat()  # Inherited method from Animal
    elephant.trumpet()  # Elephant's own method

    print("\nHybrid Inheritance:")
    copier = Copier()
    copier.print_doc()  # Inherited from Printer
    copier.scan_doc()  # Inherited from Scanner
    copier.copy_doc()  # Copier's own method

if __name__ == "__main__":
    main()
