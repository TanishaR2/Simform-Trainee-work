
class Cat:
    def sound(self):
        print("Meow!")

class Dog:
    def sound(self):
        print("Bark!")


def animal_sound(animal):
    animal.sound()

cat = Cat()
dog = Dog()

animal_sound(cat) 
animal_sound(dog)  
