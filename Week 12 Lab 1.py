#!/usr/bin/env python3.7

#Python implementation goes here

#Type chmod u+x ~/to-celsius.py command

fahrenheit = float(input("What temparature (in Fahrenheit) would you like converted to Celsius? "))
celsius = (fahrenheit - 32) * 5 / 9

print(fahrenheit, "F is", round(celsius, 2), "C")


