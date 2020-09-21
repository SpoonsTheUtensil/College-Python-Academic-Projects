'''
Created on Oct 7, 2019

@author: 16368
'''

class NoWeightEnteredError(Exception):
    
    def __init__(self, value):
        self.value = value
        
class IncorrectIndexError(Exception):
    
    def __init__(self, value):
        self.value = value


# Creates variables
peopleWeight = []
num_Weights = 4
loop = 1

while loop == 1:
    try:
        for i in range(num_Weights):
            singleWeight = float(input("Enter weight %d: " % (i + 1)))
            peopleWeight.append(singleWeight)
        for item in peopleWeight:
            if item == "":
                raise NoWeightEnteredError('Invalid weight somewhere.')
    finally:
        print()
        print("Weights: ", peopleWeight)

    # Output average
    avgWeight = sum(peopleWeight) / len(peopleWeight)
    print("Average weight: %.2f" % avgWeight)

    # Output Max Weight
    print("Max weight: %.2f" % max(peopleWeight))

    index = int(input("Enter an index number: (1 - 4)\n"))
    chosenWeight = peopleWeight[index - 1]

    print("Weight in pounds: %.2f" % chosenWeight)
    print("Weight in kilograms: %.2f" % (chosenWeight / 2.2))
        
    # Sort the list
    peopleWeight.sort()
    print("Sorted List:", peopleWeight)

    peopleWeight.sort(reverse = True)
    print("Rev. Sorted List:", peopleWeight)
    
    loop -= 1
