'''
Created on Sep 2, 2019

@author: 16368
'''

import math

# Enter an integer
userInt = int(input("Enter an integer: "))

# Enter a float
userFloat = float(input("Enter a float: "))

# Enter a char character
userChar = input("Enter a char: ")

# Enter a string
userString = input("Enter a string: ")

# Print all of the variable in two different orders
print(userInt, userFloat, userChar, userString)
print(userString, userChar, userFloat, userInt)

# Use the chr method to find the value of the integer
print(userInt, "converted to a character is", chr(userInt))

# Use the ord method to find the integer value of the char
print(userChar, "converted to a integer is", ord(userChar))

# Import math square a number with math
print("squared: ", math.pow(userFloat, 2))
print("cubed: ", math.pow(userFloat, 3))
