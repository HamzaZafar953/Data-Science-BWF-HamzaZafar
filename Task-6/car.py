class Car:
    #A simple attempt to represent a car
    
    def __init__(self, make, model, year):
        # Initialize attributes to describe a car
        self.make = make
        self.model = model
        self.year = year

    def get_descriptive_name(self):
        # Return a neatly formatted descriptive name
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

# Create an instance of the Car class
my_new_car = Car('audi', 'a4', 2016)

# Print the descriptive name of the car
print(my_new_car.get_descriptive_name())

