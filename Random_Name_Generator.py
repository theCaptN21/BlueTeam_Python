#!/usr/bin/env python3.7

#EC2 Random Name Generator

#Resources: 
#https://docs.python.org/3/library/random.html 
#https://pynative.com/python-generate-random-string/

import random
import string


#Random name generator function
def string_generator(size=6, string=string.ascii_letters + string.digits):
    return ''.join(random.choice(string) for _ in range(size))

department = input("Are you a member of Accounting, FinOps, or Marketing? If so, enter the dept name.\n").upper()  
    
for _ in department:
    
    if department == "Accounting" or department.lower() == "accounting":
        print("Verification in process, one moment please...")
        break
    
    elif department == "FinOps" or department.lower() == "finops":
        print("Verification in process, one moment please...")
        break
    
    elif department == "Marketing" or department.lower() == "marketing":
        print("Verification in process, one moment please...")
        break
    
    else:
        print("Error ❌: Department not verified. Enter the correct Department to gain access to this Name Generator.")
        exit()
        
number = int(input("Input the number of EC2 instances that require names: "))
    
if number < 0:
    print("Please enter at least one number: ")
elif number > 0:
    print("Input accepted")
    
#Results should be printed
print("\n...Results are being generated...\n")
print("Here are your new EC2 Instance Names!!")

for _ in range(1, number + 1):
    EC2_name = department
    unique_ID_name = EC2_name + "-" + string_generator()
    print("Your New EC2 Instance Name : ", unique_ID_name)
    
print("Please visit Katoria's name generator again!! 😊")




