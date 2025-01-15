class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @property
    def area(self):
        return 3.14 * (self._radius ** 2)

circle = Circle(5)
print(circle.radius)  # Access as an attribute
print(circle.area)    # Access as an attribute
