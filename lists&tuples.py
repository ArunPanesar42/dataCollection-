# What is a list
# Lists are commonly used to store data
# Lists are MUTEABLE
# Syntax [] is used to create a list

shopping_list = ["bread", "chocolate", "avacados", "milk"]
#                   0          1          2          3
print(type(shopping_list))
print(shopping_list)
print(shopping_list[1]) # index works by selecting each item
print(shopping_list[-2])

# To change the value of 0 in the list from "bread" to "orange"
shopping_list[0] = "orange"
print(shopping_list[0])
print(shopping_list)
# To add something to a list
shopping_list.append("ice cream")
print(shopping_list)
# To delete something from the list
shopping_list.remove("orange")
print(shopping_list)

# We can mix data types in a list
mixed_list = [1, 2, 3, "one", "two", "three"]
print(mixed_list[1:4])

# Tuples and lists are the same but Tuples are IMMUTABLE (Can not be changed)

essentials = ("Paracetomol", " Toothpaste", "Tea-bags")
print(essentials)
print(type(essentials))
essentials[0] = "Cereal" # This will not work because it is immutable

# WHat are Dictionaries
# Dictionaries use KEY VALUE pairs to save data
# The data can be retrieved by its value or the key
# Syntax = dict{} , list[], tuple()
# With in the dict we can also have lists declared

# Creating one
dev_ops_student = {
    "key": "value",
    "name": "James",
    "stream": "DevOps",
    "completed_lesson": 3,
    "completed_lesson_names": ["variables","data types", "collection"]
    #                   KEY :       0            1            2
}
print(dev_ops_student)
# confirm the type
print(type(dev_ops_student))
print(dev_ops_student["name"])
#to see lessons covered
print(dev_ops_student["completed_lesson"])
# To select "data types" from "completed_lesson_names"
print(dev_ops_student["completed_lesson_names"][1])
# Can also see the the whole list here
print(dev_ops_student.keys())
print(dev_ops_student.values())



# Adding a a lesson name to "completed_lesson_names"
dev_ops_student["completed_lesson_names"].append("Operators")
print(dev_ops_student["completed_lesson_names"])

# Changing the name of "Completed_lesson"
dev_ops_student["completed_lesson"] = 4
print(dev_ops_student["completed_lesson"])

# Deleting "data types" from "Completed lesson names"
dev_ops_student["completed_lesson_names"].remove("data types")
print(dev_ops_student["completed_lesson_names"])

# Looking into Sets
# This is unordered
car_parts = {"Wheels", "Windows", "Doors"}
print(car_parts)
print(type(car_parts))
# Sets are MUTABLE
car_parts.add("Seats")
print(car_parts)

# Frozen Sets