'''
Created on Sep 2, 2019

@author: 16368
'''
userFood = input("Enter food item name: ")

foodPrice = float(input("Enter item price: "))

amtFood = int(input('Enter item quantity: '))

total1 = amtFood * foodPrice
print()

print("RECEIPT")
print(amtFood, userFood, "@ $", foodPrice, "= $", total1)
print("Total cost: $", total1)
print()

user2Food = input("Enter second food item name: ")

food2Price = float(input("Enter item price: "))

amt2Food = int(input("Enter item quantity: "))

total2 = amt2Food * food2Price

totalBoth = total1 + total2

tip = totalBoth * 0.15

totalTip = totalBoth + tip
print()

print("RECEIPT")
print(amtFood, userFood, "@ $", foodPrice, "= $", total1)
print(amt2Food, user2Food, "@ $", food2Price, "= $", total2)
print("Total cost: $", totalBoth)
print()
print("15% gratuity: $", tip)
print("Total with tip: $", totalTip)
