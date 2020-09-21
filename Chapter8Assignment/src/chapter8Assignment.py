'''
Created on Oct 7, 2019

@author: 16368
'''
roster = {}
dictKeys = []
dictValues = []
amount_of_players = 0
d = 1
while d == 1:

    print()
    print("Menu")
    print("a - Add player")
    print("d - Remove player")
    print("u - Update player rating")
    print("r - Output players above a rating")
    print("o - Output roster")
    print("q - Quit")
    print()

    userInput = input("Choose an option: ")

    if userInput == "o":
        if amount_of_players == 0:
            print("No Players in Roster.")
            continue
        else:
            print("Roster")
            for key in sorted(roster.keys()):
                print("Jersey Number: %s, Rating: %s" % (key, roster[key]))
                
    elif userInput == "a":
        amount_of_players += 1
        jerseyNum = int(input("Enter player's jersey number: "))
        playerRating = int(input("Enter player's rating: "))
        roster[jerseyNum] = playerRating
    
        dictKeys = list(roster.keys())
        dictValues = list(roster.values())
        print("Player Added")
        
    elif userInput == "d":
        delJerseyNum = int(input("Enter a jersey number: "))
        if delJerseyNum in roster:
            del roster[delJerseyNum]
            dictKeys = list(roster.keys())
            dictValues = list(roster.values())
            amount_of_players -= 1
            print("Player Removed")
    elif userInput == "u":
        playerJersey = int(input("Enter player's jersey number: "))
        newRating = int(input("Enter a new rating for player: "))
        if playerJersey in roster:
            new = {playerJersey: newRating}
            roster.update(new)
            dictKeys = list(roster.keys())
            dictValues = list(roster.values())
            print("Player Rating Updated")
            
    elif userInput == "r":
        rating = int(input("Enter a rating: "))
        print("Players With Rating Above %d." % rating)
        for value in roster.values():
            if rating > value:
                for key in sorted(roster.keys()):
                    print("Jersey Number: %s, Rating: %s" % (key, roster[key]))
            else:
                continue
        
    elif userInput == "q":
        d = 0
    