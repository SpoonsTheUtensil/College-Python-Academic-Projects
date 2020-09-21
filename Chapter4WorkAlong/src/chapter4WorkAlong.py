'''
Created on Sep 16, 2019

@author: 16368
'''

# Create variables and constants
serviceCost = 0.00
OIL_CHANGE = 35.00
TIRE_ROTATION = 19.00
CAR_WASH = 7.00

# Enter service type
serviceChoice = input("Enter desired auto service: ")

print("You entered: " + serviceChoice)

# Evaluate service type
if serviceChoice == "Oil change":
    serviceCost = OIL_CHANGE
    print("Cost of oil change is: $%.2f" % serviceCost)
elif serviceChoice == "Tire rotation":
    serviceCost = TIRE_ROTATION
    print("Cost of tire rotation is: $%.2f" % serviceCost)
elif serviceChoice == "Car wash":
    serviceCost = CAR_WASH
    print("Cost of car wash is: $%.2f" % serviceCost)
else:
    print("Error: Requested service is not recognized.")


