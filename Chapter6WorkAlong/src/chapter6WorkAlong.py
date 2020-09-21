'''
Created on Oct 13, 2019

@author: 16368
'''

def main():
    # Enter and print string
    userStr = input("Enter a sentence or phrase: ")
    
    print("You entered: " + userStr)
    
    # Call function to get string length
    numChars = get_num_of_characters(userStr)
    print("\nNumber of characters: " + str(numChars))
    
    # Call function to remove all white SPACE
    output_without_whitespace(userStr)
    
def get_num_of_characters(userStr):
    # Function returns number of characters in a string
    numChars = 0
    
    # Loop through string to count chars
    for i in userStr:
        numChars += 1
        
    print("Use the length. Number of characters is: ", len(userStr))
    
    return numChars

def output_without_whitespace(inputStr):
    print("String with no whitespace: ", end=" ")
    
    for i in range(len(inputStr)):
        if not inputStr[i].isspace():
            print(inputStr[i], end="")
        
    print("\n", end="")
    
main()
