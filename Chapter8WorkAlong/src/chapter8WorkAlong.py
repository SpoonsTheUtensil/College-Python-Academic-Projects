'''
Created on Oct 7, 2019

@author: 16368
'''

# Creates variables
peopleWeight = []
num_Weights = 4


# Ask for user weights
for i in range(num_Weights):
    singleWeight = float(input("Enter weight %d: " % (i + 1)))
    peopleWeight.append(singleWeight)

print("Weights: ", peopleWeight)

# Output average
avgWeight = sum(peopleWeight) / len(peopleWeight)
print("Average weight: %.2f" % avgWeight)

# Output Max Weight
print("Max weight: %.2f" % max(peopleWeight))

# Ask user for list element
index = int(input("Enter an index number: (1 - 4)"))
chosenWeight = peopleWeight[index - 1]
print("Weight in pounds: %.2f" % chosenWeight)
print("Weight in kilograms: %.2f" % (chosenWeight / 2.2))

# Sort the list
peopleWeight.sort()
print("Sorted List:", peopleWeight)

peopleWeight.sort(reverse = True)
print("Rev. Sorted List:", peopleWeight)
