#This is an example of indexing a string for a single item
Input = test_str = 'testing'
Input = test_str[0]
Output = 't'

#This is an example of negative indexing 
Input = test_str[len(test_str) -1]
Input = test_str[-1]
Output = 'g'

#This is an example of how to create a slice
Input = test_str[0:2]
Output = 'te'

#This is another example of slicing
Input = test_str[2:len(test_str)]
Ouput = 'sting'

#This is an example of going from the start of an index to the end of a string
Input = test_str[2:]
Output = 'sting'

#This is an example of adding a step value to slicing
Input = test_str[1:5:2]
Output = 'et'
#1 = starting index, 5 = ending index, 2 = step value

#This is an example of slicing with a negative value
Input = test_str[::-1]
Output = 'gnitset'

