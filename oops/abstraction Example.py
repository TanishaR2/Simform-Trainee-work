from abc import ABC, abstractmethod

class Animal(ABC):
    
    @abstractmethod
    def make_sound(self):
        pass

class Dog(Animal):
    
    def make_sound(self):
        return "Woof!"

class Cat(Animal):
    
    def make_sound(self):
        return "Meow!"

def animal_sound(animal: Animal):
    print(animal.make_sound())

dog = Dog()
cat = Cat()

animal_sound(dog)
animal_sound(cat)
