class Car:
    def __init__(self, make, model, year):
		
		
        # Initialize attributes to describe a car
        
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0 

    def get_descriptive_name(self):
		
		
        # Return a neatly formatted descriptive name
        
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
		
		
        # Print a statement showing the car's mileage
        
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
		
		
        # Set the odometer reading to the given mileage
        
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
		
		
        # Add the given amount to the odometer reading
        
        self.odometer_reading += miles


# Create an instance of the Car class

my_used_car = Car('subaru', 'outback', 2013)


# Print the descriptive name of the car

print(my_used_car.get_descriptive_name())


# Update the odometer reading to 23500

my_used_car.update_odometer(23500)
my_used_car.read_odometer()


# Increment the odometer reading by 100 miles

my_used_car.increment_odometer(100)
my_used_car.read_odometer()

