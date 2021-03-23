# Data Collection in Python 

- Lists and Tuples 
- Dictionaries like an Array
- Sets 

## What is a List 
- Lists are commonly used to store data 
- Lists are MUTEABLE (Flexible)
- Syntax [] is used to create a list
### Here is our list 
````
shopping_list = ["bread", "chocolate", "avacados", "milk"]
#                   0          1          2          3
````
- The index values represent what number each item in the list is

### To change the value of 0 in the list from "bread" to "orange"
``
shopping_list[0] = "orange"
``
- this will then print:
``
 ['orange', 'chocolate', 'avacados', 'milk'] 
``
### To add something to a list we use .append(), for example 
```python
shopping_list.append("ice cream")
```
- this will then print ``['orange', 'chocolate', 'avacados', 'milk', 'ice cream']``
### To delete something from the list we use .remove()
```python
shopping_list.remove("orange")
```
- Which will give the Result 
```python
['chocolate', 'avacados', 'milk', 'ice cream']
```
## We can also mix lists 

### Here is our List 
```python
mixed_list = [1, 2, 3, "one", "two", "three"]
``` 
- When we print this we get this result:
```python
[2, 3, 'one']
```
## What is a tuple and whats the difference between that and a list
- Tuples and lists are the same but Tuples are IMMUTABLE (Can not be changed)

## What are Dictionaries 
- Disctionaries use KEY VALUE pairs to save data
- The data can be retrieved by its value or the key
```python
dict{} , list[], tuple()
```
- With in the dict we can also have lists declared 