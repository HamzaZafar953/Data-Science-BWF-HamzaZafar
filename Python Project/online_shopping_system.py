# Python Project 
                             
# Online Shopping System 

class Product:
	
#  Defines a class named Product

    def __init__(self, product_id, name, price, stock):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.stock = stock

    def update_stock(self, quantity):
		
        self.stock += quantity
        
        # Updates the stock by adding the given quantity

    def __str__(self):
		
		# Defines the string representation of the object 
		
        return f"Product ID: {self.product_id}, Name: {self.name}, Price: {self.price}, Stock: {self.stock}"

class Heavybikes (Product):
	
	    # Defines a class named Heavybikes that inherits from Product class
	
    def __init__(self, product_id, name, price, stock, brand, model, warranty_period):
        super().__init__(product_id, name, price, stock)
        
        # Calls the parent class (Product) initializer
        
        self.brand = brand
        self.model = model
        self.warranty_period = warranty_period

    def __str__(self):
        return (super().__str__() + f", Brand: {self.brand}, Model: {self.model}, Warranty Period: {self.warranty_period} months")


class Electronics(Product):
	
	    # Defines a class named Electronics that inherits from Product class
	
    def __init__(self, product_id, name, price, stock, brand, warranty_period):
        super().__init__(product_id, name, price, stock)
        
        # Calls the parent class (Product) initializer
        
        self.brand = brand
        self.warranty_period = warranty_period

    def __str__(self):
        return (super().__str__() + f", Brand: {self.brand}, Warranty Period: {self.warranty_period} months")


class Clothing(Product):
	
	    # Defines a class named Clothing that inherits from Product class
	
    def __init__(self, product_id, name, price, stock, size, material):
        super().__init__(product_id, name, price, stock)
        self.size = size
        self.material = material

    def __str__(self):
        return (super().__str__() + f", Size: {self.size}, Material: {self.material}")


class Customer:
	
    def __init__(self, customer_id, name, email, address):
		
		# The initializer method that sets up the attributes for the customer class
		
        self.customer_id = customer_id
        self.name = name
        self.email = email
        self.address = address

    def __str__(self):
        return f"Customer ID: {self.customer_id}, Name: {self.name}, Email: {self.email}, Address: {self.address}"


class Order:
    def __init__(self, order_id, customer, product, quantity):
        self.order_id = order_id
        self.customer = customer
        self.product = product
        self.quantity = quantity
        self.status = "Pending"
        
        # Sets the initial status of the order to Pending

    def process_order(self):
        if self.product.stock >= self.quantity:
			
			# Checks if the product stock is sufficient 
			
            self.product.update_stock(-self.quantity)
            
            # Updates the product stock by subtracting the ordered quantity
            
            self.status = "Completed"
            print(f"Order {self.order_id} processed successfully.")
        else:
            self.status = "Failed"
            print(f"Order {self.order_id} failed due to insufficient stock.")

    def __str__(self):
        return (f"Order ID: {self.order_id}, Customer: {self.customer.name}, Product: {self.product.name}, "
                f"Quantity: {self.quantity}, Status: {self.status}")


def main():
    products = []
    
    # Initializes an empty list for products
    
    customers = []
    
    # Initializes an empty list for customers
    
    orders = []
    
    # Initializes an empty list for orders
    

    while True:
		
		# Infinite loop
		
        print("\n\n1. Please Add Product\n2. Please Add Customer\n3. Please Place Order\n4. To View Products\n5. To View Customers\n6. To View Orders\n7. To Exit")
        choice = input(" \n\nPlease Enter your choice: ")

        if choice == '1':
            product_type = input("\nEnter product type (Heavybikes/Electronics/Clothing): ")
            product_id = int(input("Enter product ID: "))
            name = input("Enter product name: ")
            price = float(input("Enter product price: "))
            stock = int(input("Enter product stock: "))

            
            if product_type.lower() == 'heavybikes':
                brand = input("Enter brand: ")
                model = int (input ("Enter model: "))
                warranty_period = int(input("Enter warranty period (months): "))
                product = Electronics(product_id, name, price, stock, brand, warranty_period)
            
            elif product_type.lower() == 'electronics':
                brand = input("Enter brand: ")
                warranty_period = int(input("Enter warranty period (months): "))
                product = Electronics(product_id, name, price, stock, brand, warranty_period)
                
            elif product_type.lower() == 'clothing':
                size = input("Enter size: ")
                material = input("Enter material: ")
                product = Clothing(product_id, name, price, stock, size, material)
            else:
                print("\nInvalid product type!")
                continue

            products.append(product)
            print("\nProduct added successfully!")

        elif choice == '2':
            customer_id = int(input("Enter customer ID: "))
            name = input("Enter customer name: ")
            email = input("Enter customer email: ")
            address = input("Enter customer address: ")
            customer = Customer(customer_id, name, email, address)
            customers.append(customer)
            print("\nCustomer added successfully!")

        elif choice == '3':
            if not products or not customers:
                print("\nNo products or customers available to place an order.")
                continue

            order_id = int(input("Enter order ID: "))
            customer_id = int(input("Enter customer ID: "))
            product_id = int(input("Enter product ID: "))
            quantity = int(input("Enter quantity: "))

            customer = next((c for c in customers if c.customer_id == customer_id), None)
            product = next((p for p in products if p.product_id == product_id), None)

            if customer and product:
                order = Order(order_id, customer, product, quantity)
                order.process_order()
                orders.append(order)
            else:
                print("\nInvalid customer or product ID!")

        elif choice == '4':
            for product in products:
                print(product)

        elif choice == '5':
            for customer in customers:
                print(customer)

        elif choice == '6':
            for order in orders:
                print(order)

        elif choice == '7':
            break

        else:
            print("\nInvalid choice! Please try again.")


if __name__ == "__main__":
    main()
