#To perform a conditional using the if statemwnt, do the following:
Input = if 'a' < 'b':
...    print("CONDITION was true")
Output = CONDITION was true

Input = if 'b' < 'a':
...    print("CONDITION was true") 
...

Input = if False:
...    print("Was true")
... else:
...    print("Was false")
...
Output = Was false

Input = if True:
...    print("Was true")
... else:
...    print("Was false")
...
Output = Was true

#An example of making a comparison using elif is shown below:
Input = if 'b' < 'a'
...    print("This is true")
... elif 'c' < 'd':
...    print("Second condition is true")
... else:
...    print("no condition was true")
...
Output = Second condition is true

#This is another example of using if and elif statements combined:
name = input("What is your name? ")

if len(name) >= 6:
    print("Your name is long")
elif len(name) == 5:
    print("Your name is 5 characters")
elif len(name) >= 4:
    print("Your name is 4 or more characters")
else:
    print("Your name is short")

# To use the pass statement to define the else branch of the logic, do the following:
Input = 
name = "Katoria"
if name =="Katoria"
...    print("Hello Katoria")
... else:
...    pass
...



