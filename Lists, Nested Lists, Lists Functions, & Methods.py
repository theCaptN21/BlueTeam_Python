#This is an example of a list
Input = my_list = [1,2,3,4,5]
Type my_list
Output = [1, 2, 3, 4, 5]

#This is another example of a list
Input = other_list = ['a', 1, 1.0, False]
Type other_list
Output = ['a', 1, 1.0, False]

#This an an example of a list with an index
Input = my_list[0]
Output = 1

#This is an example of determining the length of a list
Input = len(my_list)
Output = 5

#This is an example of retrieving a subsection of a list using slicing
Input = my_list[0:2]
Output = [1, 2]

#This is an example of adding a step function to a list
Input = my_list[0::1]
Output = [1, 2, 3, 4, 5]

#This is an example of assigning a position in a list
Input = my list[0] = 'a'
Type my_list
Ouput = ['a', 2, 3, 4, 5]

#This is an example of concatenating a list
Input = my_list + [8, 9, 10]
Output = ['a', 2, 3, 4, 5, 8, 9, 10]

#This is an example of adding a list to a slice
Input = my_list[1:3] = ['b', 'c']
Type my_list
output = ['a', 'b', 'c', 4, 5, 8, 9, 10]

#This is an example of removing items from a list
Input = my_list = ['a', 'b', 'c', 'd', 5, 6, 7]
Input = my_list[4:] = []
Input = my_list
Output = ['a', 'b', 'c', 'd']

#This is another example of removing items from a list using the del statement
Input = del my_list[0]
Type my_list
Output = ['b', 'c', 'd']

#This is an example of adding items to a list
Input = my_list = [1, 2, 3]
Type my_list.append(4)
Type my_list
Output = [1, 2, 3, 4]

#This is an example of inserting an item to a list based on its index
Input = my_list.insert(0, 'a')
Type my_list
Output = ['a', 1, 2, 3, 4]

#This example shows you the index of an item in a list
Input = my_list = [1, 2, 3]
Type my_list.index(2)
Output = 1

#This is an example of using the "in" operation for a list
Input = my_list = [1, 2, 3]
Type 4 in my_list
Output = False
Type 4 not in my_list
Output = True

#This is an example of sorting a list
Input = my_list = [1, 3, 4, 8, 2]
Type sorted(my_list)
Ouput = [1, 2, 3, 4, 8]

#This is an example of reversing a list
Input = my_list = [1, 3, 4, 8, 2]
Type list(reversed(my_list)
Output = [2, 8, 4, 3, 1]

#This is an example of reverting a list from higher to lower numbers
Input = my_list = [1, 3, 4, 8, 2]
Type list(reversed(sorted(my_list)))
Output = [8, 4, 3, 2, 1]

#This is an example of creating a matrix for a list
Input = my_matrix = [[1, 2, 3], 
                    [4, 5, 6]]
Type my_matrix
Output = [[1, 2, 3], [4, 5, 6]]
Type row count = len(my_matrix)
Type row count
output = 2
Type column_count = len(my_matrix[0])
Type column count
Output = 3

