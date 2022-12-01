#This is an example of creating a tuple
Input = point = (2.0, 3.0)
Input = point_3d = point + (4.0,)
Type point_3d
output = (2.0, 3.0, 4.0)

#This is an example of unpacking a tuple
Input = x, y, z = point_3d
Type x
Output = 2.0
Type y
Output = 3.0
Type z
Ouput = 4.0

#This is another example of unpacking a tuple (Mainly used in Python 2)
print("My name is: %s %s" % ("Katoria", "H."))
Output = My name is: Katoria H.

#This is an example of creating items in tuples
Input = person = ('Katoria H.', 62, "555-555-5555")
Input = person2 = ('Chris Stein', 71, '')
Type person[0]
Output = 'Katoria H.'
Type person2[0]
Output = 'Chris Stein'

#This is an example of putting a list in a tuple
Input = my_list = [1, 2, 3]
Input = my_tuple = (my_list, 1)
Type my_tuple
Output = ([1, 2, 3], 1)

#This is an example of modifying a tuple that includes a list
Input = my_list.append(1)
Type my_tuple
Output = ([1, 2, 3, 1], 1)

