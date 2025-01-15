class Vehicle:
    def move(self):
        print("Vehicle moves")

class Car(Vehicle):
    def drive(self):
        print("Car drives")

class ElectricCar(Car):  # ElectricCar is a subclass of Car, which is a subclass of Vehicle
    def charge(self):
        print("Electric car is charging")

def main():
    print("\nMultilevel Inheritance:")
    electric_car = ElectricCar()
    electric_car.move()  # Inherited method from Vehicle
    electric_car.drive()  # Inherited method from Car
    electric_car.charge()  # ElectricCar's own method


if __name__ == "__main__":
    main()
