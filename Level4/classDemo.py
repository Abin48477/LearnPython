# Create a class for cars.
class Car:
    # Set up each new car.
    def __init__(self, color, model):
        # Save the car's color.
        self.color = color
        # Save the car's model.
        self.model = model

# Create the first car.
car_1 = Car("red", "Toyota Corolla")
# Create the second car.
car_2 = Car("green", "Lamborghini Revuelto")

# Show the first car's model.
print(car_1.model)
# Show the first car's color.
print(car_1.color)

# Show the second car's model.
print(car_2.model)
# Show the second car's color.
print(car_2.color)
