'''
Created on Sep 8, 2019

@author: 16368
'''
import math

height = int(input("Enter wall height (feet): "))
width = int(input("Enter a wall width (feet): "))
wallArea = height * width
paintNeeded = wallArea / 350
cansNeeded = math.ceil(paintNeeded)

print("Wall area: " + str(wallArea) + " square feet")
print("Paint needed: %f gallons" % (paintNeeded))
print("Cans needed: %d can(s)" % (cansNeeded))
print()

paintColorCost = {
    'red' : 35,
    'blue' : 25,
    'green' : 23
    }
userColor = input("Choose a color to paint the wall: ")
print("Cost of purchasing %s paint: $%d" % (userColor, paintColorCost[userColor]))