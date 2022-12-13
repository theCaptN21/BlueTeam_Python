#!/usr/bin/env python3

#To get input from an external file use this format:
with open(filename, 'r' ) as variable_name:
    <Do something with the variable here>

#Creating new files
def open_input(file):
    with open(file, 'r') as f:
        text = f.read() #We use read() to read the actual contents of the file
        print(text)

def main():
    open_input("The Quick Brown Fox")

if __name__=="__main__":
    main()

