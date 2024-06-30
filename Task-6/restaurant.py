class Restaurant:
	
    # A simple attempt to model a restaurant


    def __init__(self, restaurant_name, cuisine_type):
		
        # Initialize restaurant name and cuisine type attributes
        
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type


    def describe_restaurant(self):
		
        # Prints restaurant's name and cuisine type
        
        print(f"Restaurant Name: {self.restaurant_name}")
        print(f"Cuisine Type: {self.cuisine_type}")


    def open_restaurant(self):
		
        # Print a message indicating that the restaurant is open
        
        print(f"{self.restaurant_name} is now open.")


# Creating an instance of the Restaurant class

restaurant = Restaurant('Montano Restaurant', 'Italian')


# Printing the attributes individually

print("Restaurant Name:", restaurant.restaurant_name)
print("Cuisine Type:", restaurant.cuisine_type)


# Calling the methods

restaurant.describe_restaurant()
restaurant.open_restaurant()

