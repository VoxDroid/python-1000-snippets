# Factory Pattern

## Description
This snippet implements a factory method to create different types of objects based on input.

## Code
```python
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

vehicle = VehicleFactory.create_vehicle("car")
print(vehicle.drive())
```

## Output
```
Driving a car
```

## Explanation
- **Factory Pattern**: `VehicleFactory` creates `Car` or `Bike` instances based on a type string.
- **Logic**: Centralizes object creation logic for extensibility.
- **Complexity**: O(1) for creation.
- **Use Case**: Used when object creation logic is complex or varies by type.
- **Best Practice**: Use for polymorphic object creation; validate input types.