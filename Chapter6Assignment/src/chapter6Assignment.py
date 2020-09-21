'''
Created on Oct 13, 2019

@author: 16368
'''

import re

def get_num_of_non_WS_characters(string):
    count = len(re.findall('[^ ]', string))
    
    return count

def get_num_of_words(string):
    
    return len(string.split())

def fix_capitalization(string):
    stringNew = string[0].upper()
    i = string.split(".")
    last = ""
    count = 0
    for j in i:
        meh = True
        for l in j:
            if(l == " "):
                last += l
            elif(meh):
                if(l.islower()):
                    count += 1
                    last += l.upper()
                    meh = False
            else:
                last += l
        last += "."
    print("number of letters capitalized:", count)
    print("Edited text:", stringNew + last[1:-1])
    
    return count

def replace_punctuation(string, exclamationCount = 0, semicolonCount = 0):
    tempString = ""
    for i in string:
        if i == "!":
            exclamationCount += 1
            tempString += "."
        elif i == ";":
            semicolonCount += 1
            tempString += ','
        else:
            tempString += i
    print("Punctuation replaced.")
    print("ExclamationCount:", exclamationCount)
    print("SemicolonCount:", semicolonCount)
    print("Edited Text:", tempString)
    
    return tempString

def shorten_space(string):
    
    return " ".join(string.split())

def print_menu():
    
    print("Menu")
    print("c - Number of non-whitespace characters")
    print("w - Number of words")
    print("f - Fix capitalization")
    print("r - Replace punctuation")
    print("s - Shorten Spaces")
    print("q - Quit")
    
def main():
    
    user_input = input("Enter a sample text:")
    print("You entered:", user_input)
    print_menu()
    
    while(True):
        user_choose = input("Choose an option:")
        
        if user_choose == 'c':
            print("Number of non-whitespace characters:", get_num_of_non_WS_characters(user_input))
        elif user_choose == 'w':
            print("Number of words:", get_num_of_words(user_input))
        elif user_choose == 'f':
            fix_capitalization(user_input)
        elif user_choose == 'r':
            replace_punctuation(user_input)
        elif user_choose == 's':
            print(shorten_space(user_input))
        elif user_choose == 'q':
            print("See ya!")
            break
        else:
            print("Error: Please enter a valid option.")
            
main()