# Define a list

fruits = ["mango", "peach", "pineapple"]


# Accessing elements of a list

first_fruit = fruits[0]
second_fruit = fruits[1]
third_fruit = fruits[2]

print("First fruit:", first_fruit)
print("Second fruit:", second_fruit)
print("Third fruit:", third_fruit)


# Adding elements 

fruits.append("banana")
print("List after adding a fruit:", fruits)


# Inserting elements at a specific position

fruits.insert(2, "guava")
print("List after inserting a fruit:", fruits)


# Removing elements from a list

fruits.remove("banana")
print("List after removing a fruit:", fruits)


# Popping the last element from the list

popped_fruit = fruits.pop()
print("Popped fruit:", popped_fruit)
print("List after popping a fruit:", fruits)


# Popping an element from a specific position

popped_fruit = fruits.pop(1)
print("Popped fruit from index 1:", popped_fruit)
print("List after popping a fruit from index 1:", fruits)


# Changing an element in a list

fruits[0] = "apricot"
print("List after changing the first fruit:", fruits)


# Iterating through a list

for fruit in fruits:
    print("Fruit:", fruit)


# Finding the length of a list

print("Length of the list:", len(fruits))


# Checking if an element exists in a list

if "cherry" in fruits:
    print("Cherry is in the list")
else:
    print("Cherry is not in the list")


# Sorting a list

fruits.sort()
print("Sorted list:", fruits)


# Reversing a list

fruits.reverse()
print("Reversed list:", fruits)


# Creating a list with a range of numbers

numbers = list(range(1, 6))
print("List of numbers:", numbers)

