#Here is an example of using the 'while' loop:
Input = count = 1
while count <=:
...    print("looping")
...    count += 1
Output = 
looping
looping
looping
looping

#Here is an example of using the 'for' loop
Input = colors = ['blue', 'green', 'red', 'purple']
for color in colors:
    print(color)
Output = 
blue
green
red
purple

#Here is an example of using a tuple in a 'for' loop:
point = (1, 2, 3)
for value in point:
    print(value)
Output = 
1
2
3
ages = {'katoria': 21, 'john':38, 'kris': 27}
for key in ages:
    print(key)
Output = 
katoria
john
kris
-OR-
for key, value in ages.items()
    print(key, value)
Output = 
katoria 21
john 38
kris 27

#This is using the 'for' loop with strings:
for letter in 'my_string':
    print(letter)
Output = 
m
y
_
s
t
r
i
n
g

#Nesting loops and conditionals:
while counter <= 25:
    if counter % 4 == 0:
        print(counter)
    counter += 1
Output = 
4
8
12
16
20
24

#Loop executions:
count = 0
while count < 10:
    if count % 2 == 0:
        count += 1
        continue
    print(f"We're counting odd numbers: {count}")
    count += 1
Output  = 
We're counting odd numbers: 1
We're counting odd numbers: 3
We're counting odd numbers: 5
We're counting odd numbers: 7
We're counting odd numbers: 9

#Loop executions using 'break':
count = 1
while count < 10:
    if count % 2 == 0:
        break
    print(f"We're counting odd numbers: {count}")
    count += 1
Output = 
We're counting odd numbers: 1

#Loop executions using 'for' and 'break'
colors = ['blue', 'green', 'red', 'purple']
for color in colors:
    if color == 'blue':
        continue
    elif color == 'red':
        break
    print(color)
Output = 
green

#Integrating 'else' with loops:
count = 1
while count <= 4:
    print(count)
    count += 1
else:
    print("While loop completed")
Output = 
1
2
3
4
Wile loop completed

#Integrating 'else' with the 'for' loop:
for i in [1, 2, 3, 4 5]:
    print(i)
else:
    print("For loop completed")
Output = 
1
2
3
4
5
For loop completed

#Using 'for' loops and the 'if' statement, along with 'break':
colors = ['red', 'green' 'purple', 'black', 'blue']
for color in colors:
    if color == 'black':
        print('Black is in the list')
        break
else:
    print("Black is not in the list")
Output = 
Black is in the list

#Iterating with a range:
my_range = range(10)
my_range
Output = range(0, 10)
list(my_range)
Output = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

#Full way of creating a range:
list(range(1, 14, 2))
Output = [1, 3, 5, 7, 9, 11, 13]

#Creating a 'while' and 'for' loop with ranges:
count = 1
while count <= 4:
    print("looping")
    count += 1
Output = 
looping
looping
looping
looping
-OR-
for _ in range(4):
    print("looping")
Output = 
looping
looping
looping
looping

#Example using a 'for' loop with a list
colors = ['red', 'brown', 'pink', 'orange', 'blue']
uppercase_colors = []
for color in colors:
    uppercase_colors.append(color.upper())
uppercase_colors
Output = ['RED', 'BROWN', 'PINK', 'ORANGE', 'BLUE']


#List comprehensions using a 'for' loop:
colors = ['red', 'brown', 'pink', 'orange', 'blue']
uppercase_colors = [color.upper() for color in colors]
uppercase_colors
Output = ['RED', 'BROWN', 'PINK', 'ORANGE', 'BLUE']

#List comprehensions using a filter and the 'for' loop
warm_colors = []
for color in colors:
    if color in ['red', 'pink', 'orange']:
        warm_colors.append(color)
warm_colors
Output = ['red', 'pink', 'orange']

#List comprehensions using a filter, the 'for' loop, and 'if' statement:
colors = ['red', 'brown', 'pink', 'orange', 'blue']
warm_colors = [color for color in colors if color in ['red', 'pink', 'orange']]
warm_colors
Output = ['red', 'pink', 'orange']



    








    
    
    
