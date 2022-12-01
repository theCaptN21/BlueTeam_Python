#This is an example of creating a dictionary
Input = ages = { 'katoria': 21, 'susie': 25, 'jim': 30 }
Type ages
Output = { 'katoria': 21, 'susie': 25, 'jim': 30 }

#This is an example of indexing a dictionary
Input = ages['katoria']
Output = 21

#This is an example of adding to a dictionary (using the example text from above)
Input = ages['kim'] = 33
Type ages
Output = { 'katoria': 21, 'susie': 25, 'jim': 30, 'kim': 33 }

#This is an example of reassigning a value for a dictionary (sample text from above)
Input = ages['katoria'] = 31
Type ages
Output = { 'katoria': 31, 'susie': 25, 'jim': 30, 'kim': 33 }

#This is an example of using a dict class
Input = weights = dict(katoria=165, susie=135, jim=220)
Type weights
Output = {'katoria': 165, 'susie':135, 'jim':220}

#This is an example of using a tuple in a dict class
Input = colors = dict(['katoria', 'red'), ('susie', 'blue'), ('jim', 'green')])
Type colors
Output = {'katoria': 'red', 'susie': 'blue', 'jim': 'green'}

#This is an example of using the keys method for a dictionary
Input = ages = {'katoria:' 21, 'jim': 30}
Type ages.keys()
Output = dict_keys(['katoria', 'jim'])

#This is an example of giving the list back the keys (using sample text from above)
Input = list(ages.keys())
Output = ['katoria', 'jim']

#This is an example of creating dict values (using same text from above)
Input = ages.values()
Output = dict.values([21, 30])

#This is an example of creating dict items (using sample text from above)
Input = ages.item()
Output = dict_items([('katoria', 21), ('jim', 30)])
Type list(ages.items()) to create a lits
Output = [('katoria', 21), ('jim', 30)]

