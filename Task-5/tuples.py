# Define a tuple

fellow = ("Hamza", 24, "Engineer")


# Accessing elements of a tuple

name = fellow[0]
age = fellow[1]
profession = fellow[2]

print("Name:", name)
print("Age:", age)
print("Profession:", profession)


# Concatenate tuples 

new_fellow = fellow + ("Islamabad",)
print("Updated Tuple:", new_fellow)


# Tuple unpacking

name, age, profession = fellow
print("Unpacked Values - Name:", name, "Age:", age, "Profession:", profession)


# Nested tuples

nested_tuple = (fellow, ("Ali", 23, "Doctor"))
print("Nested Tuple:", nested_tuple)


# Iterate through a tuple

for item in fellow:
    print(item)
    

# Finding the length of a tuple

print("Length of tuple:", len(fellow))

# Checking if an element exists in a tuple

if "Hamza" in fellow:
    print("Hamza is in the tuple")

