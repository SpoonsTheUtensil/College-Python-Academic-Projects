'''
Created on Sep 2, 2019

@author: 16368
'''

userLemonJuice = float(input("Enter amount of lemon juice (in cups): "))

userAmtWater = float(input("Enter amount of water (in cups): "))

userAmtAgaveNectar = float(input("Enter amount of agave nectar (in cups): "))

userServings = float(input("How many servings does this make? "))

ingredAmount = userServings / 6

cupConvert = float(16)
print()

print("Lemonade ingredients - yields", userServings, "servings.")
print((userLemonJuice * ingredAmount) / cupConvert, "gallon(s) of lemon juice.")
print((userAmtWater * ingredAmount) / cupConvert, "gallon(s) of water.")
print((userAmtAgaveNectar * ingredAmount) / cupConvert, "gallon(s) of agave nectar.")
