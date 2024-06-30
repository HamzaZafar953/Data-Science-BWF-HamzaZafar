# Define a dictionary

person = {
    "name": "Hamza",
    "age": 24,
    "city": "Islamabad"
}


# Accessing elements

name = person["name"]
age = person["age"]
city = person["city"]

print("Name:", name)
print("Age:", age)
print("City:", city)


# Adding an element

person["email"] = "hamzazafar@example.com"
print("Dictionary after adding an email:", person)


# Changing an element 

person["age"] = 25
print("Dictionary after changing the age:", person)


# Removing an element 

del person["city"]
print("Dictionary after removing the city:", person)


# Using the pop method to remove an element

email = person.pop("email")
print("Popped email:", email)
print("Dictionary after popping the email:", person)


# Iterating through a dictionary

for key, value in person.items():
    print(f"{key}: {value}")


# Checking if a key exists in a dictionary

if "name" in person:
    print("Name is in the dictionary")
else:
    print("Name is not in the dictionary")


# Getting the length of a dictionary

print("Length of the dictionary:", len(person))


# Using the get method to access an element

name = person.get("name")
print("Name using get method:", name)


# Using the keys method to get all keys

keys = person.keys()
print("Keys in the dictionary:", keys)


# Using the values method to get all values

values = person.values()
print("Values in the dictionary:", values)


# Using the items method to get all key-value pairs

items = person.items()
print("Items in the dictionary:", items)


# Clearing all elements from the dictionary

person.clear()
print("Dictionary after clearing all elements:", person)

