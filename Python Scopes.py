#This is an example of using a scope:
if 1 < 2:
    x = 5

while x < 6:
    print(x)
    x += 1
    
print(x)
#Type python3.7 <filename>.py and the Output should look similar to this:
5
6

#This is an example of scoping using parameters and arguments with functions:
y = 5


def set_x(y): #This is sometimes called shadowing
    print("Inner y:", y)
    x = y
    y = x
    
    
set_x(10)

print("Outer y:", y)
#To run this in the terminal, type python3.7 <filename>.py, and this should be the output:
Inner y: 10
Outer y: 5

#This is an example of scoping using the global keyword:
y = 5


def set_x(z): #This is sometimes called shadowing
    x = z
    global a
    x = y
    print("X is:", x)
    a = 7
    
    
print("y before set_x:", y)

set_x(10)
print("y after set_x:", y)
print("a after set_x:", a)
#To run this in the terminal, type python3.7 <filename>.py, and this should be the output:
y before set_x: 5
X is: 5
y after set_x: 5
a after set_x: 7


