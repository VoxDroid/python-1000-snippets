# sample1.py
# simple vehicle factory (from README)

class Vehicle:
    def drive(self):
        pass

class Car(Vehicle):
    def drive(self):
        return "Driving a car"

class Bike(Vehicle):
    def drive(self):
        return "Riding a bike"

class VehicleFactory:
    @staticmethod
    def create_vehicle(type_):
        if type_ == "car":
            return Car()
        elif type_ == "bike":
            return Bike()
        raise ValueError("Unknown vehicle type")

if __name__ == '__main__':
    vehicle = VehicleFactory.create_vehicle("car")
    print(vehicle.drive())
