'''
Created on Sep 30, 2019

@author: 16368
'''

# Create variables
comma = ','
inputString = ''
firstString = ''
secondString = ''

# Loop until input is q
while inputString != 'q':
    inputString = input("Enter input string: (\'q\' to quit) ")
    
    while inputString.find(comma) == -1 and inputString != 'q':
        print("Error: No comma in string")
        inputString = input("Enter input string: (\'q\' to quit)")
    
    if inputString != 'q':
        myTokens = inputString.split(comma)
        firstStringSize = len(myTokens[0])
        
        # Test is last char is space
        if myTokens[0][firstStringSize - 1].isspace():
            firstString = myTokens[0][0:firstStringSize - 1]
        else:
            firstString = myTokens[0]
        # Test if first char of second is a space
        if myTokens[1][0].isspace():
            secondString = myTokens[1][1:]
        else:
            secondString = myTokens
        
        print(firstString)
        print(secondString)
        print()





