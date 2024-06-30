# Define a set

fruits = {"apple", "banana", "mango"}
print("Initial set of fruits:", fruits)


# Adding an element 

fruits.add("orange")
print("Set after adding 'orange':", fruits)


# Adding multiple elements 

fruits.update(["peach", "grape"])
print("Set after adding 'peach' and 'grape':", fruits)


# Removing an element 

fruits.remove("banana")
print("Set after removing 'banana':", fruits)


# Removing an element using discard 

fruits.discard("pineapple")
print("Set after discarding 'pineapple' (which does not exist):", fruits)


# Removing an element using pop 

removed_fruit = fruits.pop()
print("Removed fruit using pop:", removed_fruit)
print("Set after pop operation:", fruits)


# Checking if an element exists in a set

if "apple" in fruits:
    print("Apple is in the set")
else:
    print("Apple is not in the set")


# Iterating through a set

for fruit in fruits:
    print("Fruit:", fruit)


# Getting the length of a set

print("Number of fruits in the set:", len(fruits))


# Clearing all elements from the set

fruits.clear()
print("Set after clearing all elements:", fruits)


# Creating another set

veggies = {"carrot", "broccoli", "spinach"}


# Set intersection operation

intersection_set = fruits.intersection(veggies)
print("Intersection of fruits and veggies:", intersection_set)


# Set difference operation

difference_set = veggies.difference(fruits)
print("Difference of veggies and fruits:", difference_set)


# Set symmetric difference operation

symmetric_difference_set = veggies.symmetric_difference(fruits)
print("Symmetric difference of veggies and fruits:", symmetric_difference_set)

