#Using the 'return' value with a function
# A function that returns hello world
def hello_world():
    return 'hello world'

# Assign the hello_world() function to a variable.
greeting = hello_world()
print(greeting)

#Boto3 example with a function and variables
import boto3

client = boto3.client('translate')

#### Add the new text below this line ####

def translate_text(): # declare the function using def, name, braces for parameters and a colon  
    response = client.translate_text(
        Text='I am an AWS coding monster', # Assigning the value of the string to the variable Text
        SourceLanguageCode='en', # We are using a two letter language code from the documentation (en = English)
        TargetLanguageCode='fr' # We use a second two letter language code from the documentation (fr = French)
    )
#Modify the function
import boto3

client = boto3.client('translate')

def translate_text(): 
    response = client.translate_text(
        Text='I am an AWS coding monster', 
        SourceLanguageCode='en', 
        TargetLanguageCode='fr' 
    )
#### Add the new text below this line ####
    print(response) # this code is inside the function and will print the contents of the variable 'response' 

translate_text() # This line will call our function. Without it, python will not do anything.



#Another example of using Boto3 for functions
import boto3

client = boto3.client('translate')

def translate_text():
    response = client.translate_text(
        Text='I am an AWS coding monster',
        SourceLanguageCode='en',
        TargetLanguageCode='fr'
    )
    print(response) # this code is inside the function and will print the contents of the variable 'response'

def main():
    translate_text()

if __name__=="__main__":
    main()
    
    
    
#Example of positional arguments
import boto3

def translate_text():
    client = boto3.client('translate')
    response = client.translate_text(
        Text='I am an AWS coding monster', 
        SourceLanguageCode='en', 
        TargetLanguageCode='fr' 
    )
    print(response) 

def main():
    translate_text()

if __name__=="__main__":
    main()
#Amending the function to add positional arguments
import boto3

def translate_text(text, source_language_code, target_language_code): # we define the positional arguments in the ()
    client = boto3.client('translate')
    response = client.translate_text(
        Text=text, # we remove the hard coded value
        SourceLanguageCode=source_language_code, # we used the positional argument instead
        TargetLanguageCode=target_language_code
    )
    print(response) 

def main():
    translate_text('I am an AWS coding monster','en','fr') # we provide the value for the arguments when we call the function in the correct positional order.

if __name__=="__main__":
    main()

#Using keyword arguments
import boto3

def translate_text(text, source_language_code, target_language_code): 
    client = boto3.client('translate')
    response = client.translate_text(
        Text=text, 
        SourceLanguageCode=source_language_code, 
        TargetLanguageCode=target_language_code
    )
    print(response) 

def main():
    translate_text('I am an AWS coding monster','en','fr')

if __name__=="__main__":
    main()
#Replacing positional arguments with keyword arguments
import boto3

def translate_text(**kwargs): 
    client = boto3.client('translate')
    response = client.translate_text(**kwargs)
    print(response) 

def main():
    translate_text(Text='I am an AWS coding monster',SourceLanguageCode='en',TargetLanguageCode='fr')

if __name__=="__main__":
    main()



#Using dictionaries as keyword arguments
import boto3

def translate_text(**kwargs): 
    client = boto3.client('translate')
    response = client.translate_text(**kwargs)
    print(response) 

### Change below this line only ###

kwargs={
    "Text":"I am an AWS coding monster",
    "SourceLanguageCode":"en",
    "TargetLanguageCode":"fr"
    }

def main():
    translate_text(**kwargs)

if __name__=="__main__":
    main()

