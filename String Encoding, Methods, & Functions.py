#This is an example of an encoding type
Input = ord('a')
Output = 97

#This is an example of using a hexidecimal notation in UTF
Input = 0X2122
Output = 8482

#This is an example of using a string using unicode
Input = ord('\u2122')
Output = 8482

#This is an example of using the chr function to go back to a string
Input = chr(8482)
Output = 'TM'

#This is an example of calling a method on a string object using lower and upper
Input = my_str.lower()
Output = 'testing'
Input = my_str.upper()
Output = 'TESTING'

#This is an example of creating a Capitalized string
Input = my_str = 'tEsTing'
Type my_str.capitalize()
Output = 'Testing'

#To title case a string, do the following:
Input = "This is a multiword String".title()
Output = 'This Is A Multiword Sring'

#To compare one string to another using the lower method, do the following:
Input = "Katoria@example.com".lower() == "katoria@example.com"
Output = True

#To check the context of a string, do the following:
Input = my_str.isascii()
Output = True
Input = my_str.islower()
Ouput = False
Input = my_str.isupper()
Output = False
Input = my_str.istitle()
Output = False

#This is how you call a new string and call another method onto that string
Input = my_str.title().istitle()
Output = True

#This example shows you how to determine if something is written in decimal notation
Input = "1".isdecimal()
Input = "11".isdigit()
Input = "10".isnumeric()
Output = True

#To determine if something is alphabetical, do the following:
Input = "adatcdatcd".isalpha()
Output = True

#To split a phrase, do the following:
Input = phrase = "This is super simple"
Input = words = phrase.spli()
Type words
Output = ['This', 'is', 'super', 'simple']

#To split a URL for something specific, do the following:
Input = url = "https://example.com/user/katoria"
Input = user = url.split('/')[-1]
Type user
Ouput = 'katoria'

#To split a URL in general, do the following:
Input = url = "https://example.com/user/katoria"
Input = url.split('/')
Output = ['https:', '', 'example.com', 'users', 'katoria']

#To call the join method and create a string, do the following:
Input = phrase = "This is super simple"
Input = ", ".join(words)
Output = 'This, is, super, simple'

#To call the join method and create new lines, do the following:
Input = lines = ['First line', 'Second line', 'Third line']
Type output = '\n'.join(lines)
print(output)
Output = 
First Line
Second line
Third line

#To call the format method, do the following:
Input = template = "Hello, my name is {}, and I really enjoy {}, Have a nice day!"
Type template.format('Katoria', 'Python')
Output = 'Hello, my nmae is Katoria, and I really enjoy Python, Have a nice day!'
