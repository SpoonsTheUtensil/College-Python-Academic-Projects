'''
Created on Sep 16, 2019

@author: 16368
'''

# Initialize some variables and constants for service prices
serviceCost1 = 0.00
serviceCost2 = 0.00
OIL_CHANGE = 35.00
TIRE_ROTATION = 19.00
CAR_WASH = 7.00
CAR_WAX = 12.00

# Output the menu and prices for the services
print("Davy's auto shop services")
print("Oil change -- $%.2f" % OIL_CHANGE)
print("Tire rotation -- $%.2f" % TIRE_ROTATION)
print("Car wash -- $%.2f" % CAR_WASH)
print("Car wax -- $%.2f" % CAR_WAX)

print()

# Inputs tied to variables
# Then turns the input into lower case characters for my own formatting preference
# Then initializing some total cost variables
serviceChoice1 = input("Select first service: \n")
serviceChoice1Lower = serviceChoice1.lower()
serviceChoice2 = input("Select second service: \n")
serviceChoice2Lower = serviceChoice2.lower()
total1 = 0.00
total2 = 0.00

# Checking what was typed into input
# Then giving a variable the cost of the service
if serviceChoice1Lower == "oil change":
    serviceCost1 = OIL_CHANGE
    total1 = serviceCost1
    
elif serviceChoice1Lower == "tire rotation":
    serviceCost1 = TIRE_ROTATION
    total1 = serviceCost1
    
elif serviceChoice1Lower == "car wash":
    serviceCost1 = CAR_WASH
    total1 = serviceCost1
    
elif serviceChoice1Lower == "car wax":
    serviceCost1 = CAR_WAX
    total1 = serviceCost1

if serviceChoice2Lower == "oil change":
    serviceCost2 = OIL_CHANGE
    total2 = serviceCost2
    
elif serviceChoice2Lower == "tire rotation":
    serviceCost2 = TIRE_ROTATION
    total2 = serviceCost2
    
elif serviceChoice2Lower == "car wash":
    serviceCost2 = CAR_WASH
    total2 = serviceCost2
    
elif serviceChoice2Lower == "car wax":
    serviceCost2 = CAR_WAX
    total2 = serviceCost2

#Beginning of the if statement for checking whether a dash was input 
# and if it was used to output the appropriate information
if serviceChoice1Lower == "-" and serviceChoice2Lower == "-":
    serviceCost1 = "No Service"
    serviceCost2 = "No Service"
    totalBoth = total1 + total2
    
    print("Davy's auto shop invoice")
    print()
    print("Service 1: %s" % serviceCost1)
    print("Service 2: %s" % serviceCost2)
    print()
    print("Total: $%.2f" % totalBoth)

elif serviceChoice1Lower == "-":
    serviceCost1 = "No Service"
    totalBoth = total1 + total2
    
    print("Davy's auto shop invoice")
    print()
    print("Service 1: %s" % serviceCost1)
    print("Service 2: %s, $%.2f" % (serviceChoice2, serviceCost2))
    print()
    print("Total: $%.2f" % totalBoth)
    
elif serviceChoice2Lower == "-":
    serviceCost2 = "No Service"
    totalBoth = total1 + total2
    
    print("Davy's auto shop invoice")
    print()
    print("Service 1: %s, $%.2f" % (serviceChoice1, serviceCost1))
    print("Service 2: %s" % serviceCost2)
    print()
    print("Total: $%.2f" % totalBoth)
else:
    totalBoth = total1 + total2
    
    print("Davy's auto shop invoice")
    print()
    print("Service 1: %s, $%.2f" % (serviceChoice1, serviceCost1))
    print("Service 2: %s, $%.2f" % (serviceChoice2, serviceCost2))
    print()
    print("Total: $%.2f" % totalBoth)
