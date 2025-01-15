
class Flyable:
    def fly(self):
        print("Can fly")

class Swimmable:
    def swim(self):
        print("Can swim")

class Duck(Flyable, Swimmable):  # Inheriting from both Flyable and Swimmable
    def quack(self):
        print("Duck quacks")

def main():
    print("\nMultiple Inheritance:")
    duck = Duck()
    duck.fly()  # Method from Flyable
    duck.swim()  # Method from Swimmable
    duck.quack()  # Duck's own method

if __name__ == "__main__":
    main()
