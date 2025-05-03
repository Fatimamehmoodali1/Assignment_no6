class Car:
    def __init__(self, brand):
        self.brand = brand  # Public variable

    def start(self):
        print(f"The {self.brand} car is starting.")  # Public method

# Example usage:
my_car = Car("Toyota")
print(my_car.brand)  # Accessing public variable
my_car.start()       # Calling public method
