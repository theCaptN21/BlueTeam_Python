#To define and use a function, use this example:
def print_name(name):
    print(f"Name is {name}")
    print_name("Katoria")
Output = Name is Katoria 

#Another example of using a function:
def add_two(num):
    return num + 2
result = add_two(2)
result
Output = 4

#This is an example of using multiple 'parameters' with a function:
def add(num1, num2):
    return num1 + num2
add(1, 5)
Output = 6

#To define variables inside a function, do the following:
def contact_card(name, age, car_model):
  return f"{name} is {age} and drives a {car_model}"
contact_card("Katoria", 21, "Chevy Tahoe")
Output = 'Katoria is 21 and drives a Chevy Tahoe'

#This is an example of using 'key word arguments' with a function:
def contact_card(name, age, car_model):
  return f"{name} is {age} and drives a {car_model}"
contact_card(age=21, car_model="Chevy Tahoe", name="Katoria")
Output = 'Katoria is 21 and drives a Chevy Tahoe'
    
#This is an example of using a 'positional' argument:
def contact_card(name, age, car_model):
  return f"{name} is {age} and drives a {car_model}"
contact_card("Katoria", car_model="Chevy Tahoe", age=21)
Output = 'Katoria is 21 and drives a Chevy Tahoe'

#This example function provides a boolean as a result:
def can_drive(age, driving_age=16):
    return age >= driving_age
can_drive(29)
Output = True

#This is an example of using the 'fibonacci sequence' with a function for recursion (calling a function from within itself):
1, 1, 2, 3, 5, 8, 13

f(n) = f(n - 2) + f(n - 1)

f(5) = f(3) + f(4)
f(5) = f(1) + f(2) + f(2) + f(3)
f(5) = 1 + f(0) + f(1) + f(0) + f(1) + f(1) + f(2)
f(5) = 1 + 0 + 1 + 0 + 1 + 1 + f(0) + f(1)
f(5) = 1 + 0 + 1 + 0 + 1 + 1 + 0 + 1
f(5) = 5

#This is an example of using the fibonacci function in a simplified manner (actual script):
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fib(n - 2) + fib(n -1)
item_to_calculate = int(input("What Fibonnaci item would you like to calculate? "))
print(fib(item_to_calculate))


