class Animal:
    def sound(self):
        return "Animal makes sound"

class Dog(Animal):
    def sound(self):
        return f"{super().sound()}, but Dog barks!" #overriding with dsuper keyword
    
dog = Dog()
print(dog.sound())







