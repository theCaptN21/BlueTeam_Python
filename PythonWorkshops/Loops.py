#!/usr/bin/env python3

#Using simple loops
    fruit = ['apples','oranges','bananas']

    for item in fruit:
        print(f'The best fruit now is {item}')

#Using a loop as a counter
    numbers = [0,1,2,3,4,5,6,7,8,9,10]
    for number in numbers:
        print(f'The next number is {number}')

#Using range to start counting at 1
    for number in range(1,10):
        print(f'The next number is {number}')

#Incrementing a counter by adding the paramter to the range() function
    for number in range(1,10,2):
        print(f'The next number is {number}')
        
#Looping with JSON
# Standard Imports
import argparse
import json

# 3rd Party Imports
import boto3 

# Arguments
parser = argparse.ArgumentParser(description="Provides translation  between one source language and another of the same set of languages.")
parser.add_argument(
    '--file',
    dest='filename',
    help="The path to the input file. The file should be valid json",
    required=True)

args = parser.parse_args()

# Functions
def open_input():
    """This function returns a dictionary containing the contents of the Input section in the input file""" 
    with open(args.filename) as file_object:
        contents = json.load(file_object)
    return contents['Input']

# Boto3 function to use Amazon Translate to translate the text and only return the Translated Text
def translate_text(**kwargs): 
    client = boto3.client('translate')
    response = client.translate_text(**kwargs)
    print(response['TranslatedText']) 

# Add a Loop to iterate over the json file.
def translate_loop():
    input_text = open_input()
    for item in input_text: # Here we iterate over all dictionaries in the Input list
        translate_text(**item)

# Main Function - use to call other functions
def main():
    translate_loop()

if __name__ == "__main__":
    main()

#Appending for a for loop
# Create a list of the input text
def new_input_text_list():
    input_text = open_input()
    new_list = []
    for item in input_text:
        text = item['Text']
        new_list.append(text)
    print(new_list)

def main():
    new_input_text_list()
    translate_loop()

#List comprehension with loops
def new_list_comprehension():
    input_text = open_input()
    list_comprehension = [item['Text'] for item in input_text]
    print(list_comprehension)

def main():
    new_input_text_list()
    translate_loop()
    new_list_comprehension()

