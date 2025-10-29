"""
Exercise 6: Class Methods, Static Methods, and Factory Pattern
"""
class Vehicle:

    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    @staticmethod
    def validate_price(price):
        if price <=0:
            raise ValueError("Price must be positive")
        return True

    @classmethod
    def from_string(cls, vehicle_str):
        brand, model, price = vehicle_str.split(",")
        cls.validate_price(float(price))
        return cls(brand, model, float(price))

    def __str__(self):
        return f"{self.brand} {self.model} - ₹{self.price}"

class Car(Vehicle):
    def __init__(self, brand, model, price, fuel_type="Unknown"):
        super().__init__(brand, model, price)
        self.fuel_type = fuel_type

    def __str__(self):
        return f"Car: {super().__str__()}, Fuel: {self.fuel_type}"


class Bike(Vehicle):
    def __init__(self, brand, model, price, engine_cc):
        super().__init__(brand, model, price)
        self.engine_cc = engine_cc

    def __str__(self):
        return f"Bike: {super().__str__()}, Engine: {self.engine_cc}cc"

car1 = Car.from_string("Toyota,Corolla,1800000")
bike1 = Bike("Yamaha", "MT15", 160000, 155)

print(car1)
print(bike1)
