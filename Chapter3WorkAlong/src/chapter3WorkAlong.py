'''
Created on Sep 8, 2019

@author: 16368
'''

# Enter two string and an integer (color, pet name, number)

favColor = input("Enter your favorite color: ")
petName = input("Enter your pets name: ")
userNum = int(input("Enter a number: "))

# Output all the values on a single line

print("You entered: ", favColor, petName, userNum)

# Output two passwords using the following pattern:
# PW1: firstString_secondString PW2: numfirstStringnum

password1 = favColor + "_" + petName
print("\nFirst password: " + password1)

password2 = str(userNum) + favColor + str(userNum)
print("\nSecond password: " + password2)

# Output length of PW1 and PW2
print()
print("Number of characters in %s: %d" % (password1, len(password1)))
print("Number of characters in %s: %d" % (password2, len(password2)))