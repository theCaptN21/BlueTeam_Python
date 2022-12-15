#Simple example of using the try-except block
import logging

integer = 50
string = "The number is"

try:
    print(string + integer)
except TypeError as err:
    logging.warning("Error - {}. You cannot add a string to an integer, without converting the integer to a string first".format(err))


#Example of adding multiple except statements for Errors
import logging

integer = 50
string = "The number is"

try:
    print(string + integer)
except TypeError as t_err:
    logging.warning("Error - {}. You cannot add a string to an integer, without converting the integer to a string first".format(t_err))
except ValueError as v_err:
    logging.warning("Error - {}. Your message".format(v_err))
    
#Using botocore with the try-except statement
import logging
import boto3
from botocore.exceptions import ClientError

try:
    client = boto3.client('translate')
    <snip>
except ClientError as e:
    logging.warning("<your msg> {}".format(e))


#Adding error handling to the code (see script above)
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
    required=True
    )

args = parser.parse_args()

# Functions

# Open the input file to get the json.
def open_input():
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
    for item in input_text:
        if input_validation(item) == True:
            translate_text(**item)
        else:
            raise SystemError

# Add our input validation as a function here.
def input_validation(item):
    languages = ["af","sq","am","ar","az","bn","bs","bg","zh","zh-TW","hr","cs","da","fa-AF",
                "nl","en","et","fi","fr","fr-CA","ka","de","el","ha","he","hi","hu","id","it",
                "ja","ko","lv","ms","no","fa","ps","pl","pt","ro","ru","sr","sk","sl","so","es",
                "sw","sv","tl","ta","th","tr","uk","ur","vi"
                ]
    json_input=item
    SourceLanguageCode = json_input['SourceLanguageCode']
    TargetLanguageCode = json_input['TargetLanguageCode']

    if SourceLanguageCode == TargetLanguageCode:
        print("The SourceLanguageCode is the same as the TargetLanguageCode - nothing to do")
        return False
    elif SourceLanguageCode not in languages and TargetLanguageCode not in languages:
        print("Neither the SourceLanguageCode and TargetLanguageCode are valid - stopping")
        return False
    elif SourceLanguageCode not in languages:
        print("The SourceLanguageCode is not valid - stopping")
        return False
    elif TargetLanguageCode not in languages:
        print("The TargetLanguageCode is not valid - stopping")
        return False
    elif SourceLanguageCode in languages and TargetLanguageCode in languages:
        print("The SourceLanguageCode and TargetLanguageCode are valid - proceeding")
        return True
    else:
        print("There is an issue")
        return False

# Main Function - use to call other functions
def main():
    translate_loop()

if __name__ == "__main__":
    main()

#Modifying the script to add the try-except statement (see script above)
# Standard Imports
import argparse
import json
# import logging
import logging

# 3rd Party Imports
import boto3
from botocore.exceptions import ClientError

# Set the logging file and default.  The default is 'Warning'
logging.basicConfig(filename='translate.log',level=logging.DEBUG)

# Arguments
parser = argparse.ArgumentParser(description="Provides translation  between one source language and another of the same set of languages.")
parser.add_argument(
    '--file',
    dest='filename',
    help="The path to the input file. The file should be valid json",
    required=True
    )

args = parser.parse_args()

# Functions

# Open the input file to get the json.
def open_input():
    try:
        with open(args.filename) as file_object:
            contents = json.load(file_object)
            return contents['Input']
    except FileNotFoundError as e:
        logging.warning("Error {}.  Sorry the input file could not be found, check and try again".format(e))

# Boto3 function to use Amazon Translate to translate the text and only return the Translated Text
def translate_text(**kwargs):
    try:
        client = boto3.client('translate')
        response = client.translate_text(**kwargs)
        print(response['TranslatedText'])
    except ClientError as e:
        logging.warning("Botocore generated an error {}".format(e))

# Add a Loop to iterate over the json file.
def translate_loop():
    try:
        input_text = open_input()
        for item in input_text:
            if input_validation(item) == True:
                translate_text(**item)
            else:
                raise SystemError
    except:
        logging.warning("An error has caused the translation to fail, check the logs for details")

# Add our input validation as a function here.
def input_validation(item):
    try:
        languages = ["af","sq","am","ar","az","bn","bs","bg","zh","zh-TW","hr","cs","da","fa-AF",
                    "nl","en","et","fi","fr","fr-CA","ka","de","el","ha","he","hi","hu","id","it",
                    "ja","ko","lv","ms","no","fa","ps","pl","pt","ro","ru","sr","sk","sl","so","es",
                    "sw","sv","tl","ta","th","tr","uk","ur","vi"
                    ]
        json_input=item
        SourceLanguageCode = json_input['SourceLanguageCode']
        TargetLanguageCode = json_input['TargetLanguageCode']

        if SourceLanguageCode == TargetLanguageCode:
            logging.debug("The SourceLanguageCode is the same as the TargetLanguageCode - nothing to do")
            return False
        elif SourceLanguageCode not in languages and TargetLanguageCode not in languages:
            logging.warning("Neither the SourceLanguageCode and TargetLanguageCode are valid - stopping")
            return False
        elif SourceLanguageCode not in languages:
            logging.warning("The SourceLanguageCode is not valid - stopping")
            return False
        elif TargetLanguageCode not in languages:
            logging.warning("The TargetLanguageCode is not valid - stopping")
            return False
        elif SourceLanguageCode in languages and TargetLanguageCode in languages:
            logging.info("The SourceLanguageCode and TargetLanguageCode are valid - proceeding")
            return True
        else:
            logging.warning("There is an issue")
            return False
    except:
        logging.warning("An unspecified error has occurred ")

# Main Function - use to call other functions
def main():
    translate_loop()

if __name__ == "__main__":
    main()
