#Assigning Strings to a variable
   first_name = "Katoria"
   last_name = "Python"

#Adding strings together using variables (concatenating them)
    print(first_name+last_name)
KatoriaPython

#Adding a space to a string
    print(first_name + " " + last_name)
Katoria Python

#Using the format() method in a string with multiple variables
   first_name = "Katoria"
   surname = "Doe"
   print("My first name is {}. My family name is {}".format(first_name, surname))

#Example of an f-string
firstname = "Katoria"
surname = "Doe"

print(f"My first name is {firstname}. My family name is {surname}")

#Using new lines and indentation with strings
   string = "This is a string over\nthree lines\n\twith the third line indented"
   print(string)

This is a string over
three lines
        with the third line indented
        
#Converting a variable from an integer to a string using the string() method
my_int = 50
sentence = "The total comes to: "

print(sentence + str(my_int))

#str() returns a string object
#int() returns an integer object
#float() returns a floating point object
#bool() a boolean value of True or False

#Assigning a key-value to a dictionary
    user = {"first_name":"Katoria"}
    print(user)
{'first_name': 'Katoria'}

#Reading the value associated with a key
    user = {"first_name":"Katoria"}
    print(user["first_name"])
Katoria

#Adding an additional key value to a dictionary
   user["family_name"] = "Byron"
   print(user)
{'first_name': 'Katoria', 'family_name': 'Byron'}

#Deleting a key-value pair
    del user["family_name"]
    print(user)
{'first_name': 'Katoria'}

#Assigning the values you want to store in a list to a variable
fruit = ["apples","oranges","bananas"]

#Reading an element from a list
   fruit = ["apples","oranges","bananas"]
   print(fruit[1])
oranges

#Finding the length of a list
   len(fruit)
3

#Returning the last value in a list
   print(fruit[-1])
bananas
   print(fruit[-2])
oranges

#Use the insert() methiod to add an element at a specific point in a list
    fruit.insert(2, "passion fruit")
    print(fruit)
['apples', 'oranges', 'passion fruit', 'bananas', 'kiwi']

#Using the sort() fucntion to retain the original order of a list
   print(sorted(fruit))
['apples', 'bananas', 'kiwi', 'oranges', 'passion fruit']
   print(fruit)
['apples', 'oranges', 'passion fruit', 'bananas', 'kiwi']

#Permanently sorting a list
    fruit.sort()
    print(fruit)
['apples', 'bananas', 'kiwi', 'oranges', 'passion fruit']

#Use the del statement to remove elements from a list
    del fruit[1]
    print(fruit)
['passion fruit', 'kiwi', 'bananas', 'apples']

#using pop() to return the last element in a list using the index value
    fresh_fruit = fruit.pop(1)
    print(fresh_fruit)
kiwi

#Use the remove() method to specify the value of the element to remove
    fruit.remove('bananas')
    print(fruit)
['passion fruit']

#Determining the type of data stored in a variable
   my_variable = "A string"
   print(type(my_variable))
   
#Example of a TypeError
>>> my_number = 50
>>> some_string = "The number is "
>>> print(some_string + my_number)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can only concatenate str (not "int") to str
#Fixing a type error by creating my_number to a string
    my_number = 50
    some_string = "The number is "
    print(some_string + str(my_number))
The number is 50















