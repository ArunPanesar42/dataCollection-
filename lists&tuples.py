# What is a list
# Lists are commonly used to store data
# Lists are MUTEABLE
# Syntax [] is used to create a list

shopping_list = ["bread", "chocolate", "avacados", "milk"]
# #                   0          1          2          3
# print(type(shopping_list))
# print(shopping_list)
# print(shopping_list[1]) # index works by selecting each item
# print(shopping_list[-2])

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
