from abc import ABC, abstractclassmethod

# abstract class 'shap' providing abstraction
class Shape(ABC):
    @abstractclassmethod
    def area(self):
        # abstract method to calculate area, must be implemented by subclass
        pass

    @abstractclassmethod
    def perimeter(self):
        # abstract method to calculate areperimeter, must be implemented by subclass
        pass

class Rectangle(Shape):
    def __init__(self, height, width):
        self.width = width
        self.height = height

    #getter method for width
    def get_width(self):
        return self.width
    
    #setter method for width
    def set_width(self, width):
        if width > 0:
            self.width = width
        else:
            print("Invalid width")

    #getter method for height
    def get_height(self):
        return self.height
    
    #setter method for height
    def set_height(self, height):
        if height > 0:
            self.height = height
        else:
            print("Invalid height")

    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)
    

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def get_radius(self):
        return self.radius
    
    def set_radius(self, radius):
        if radius > 0:
            self.radius = radius
        else:
            print("Invalid radius")

    def area(self):
        return 3.14159 * self.radius
    
    def perimeter(self):
        return 2 * 3.14159 * self.radius
    

def main():
    rectangle = Rectangle(10, 7)
    
    print(f"Area of Rectangle: {rectangle.area()}")
    print(f"Perimeter of Rectangle: {rectangle.perimeter()}")

    rectangle.set_width(9)
    rectangle.set_height(12)
    
    print(f"Updated Rectangle area: {rectangle.area()}")
    print(f"Updated Rectangle perimeter: {rectangle.perimeter()}")

    circle = Circle(7)

    print(f"Area of circle is {circle.area()} and perimeter of the circle is {circle.perimeter()}")

    circle.set_radius(8)
    print(f"Updated rea of circle is {circle.area()} and updated perimeter of the circle is {circle.perimeter()}")


if __name__ == "__main__":
    main()
        

    











