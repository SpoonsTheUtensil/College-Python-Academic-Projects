'''
Created on Oct 20, 2019

@author: 16368
'''

from ShoppingCart import ShoppingCart

def menu(shoppingcart):
    cart = shoppingcart
    
    if cart._currentDate == "":
        cart._currentDate = "January 1, 2016"
    d = 1
    while d == 1:
        print("Customer name: %s" % cart._customerName)
        print("Today's date: %s" % cart._currentDate)
        print()
    
        print("Menu")
        print("a - Add item to cart")
        print("r - Remove item from cart")
        print("c - Change items quantity")
        print("i - Output items' descriptions")
        print("o - Output shopping cart")
        print("q - Quit")
        print()

        user_Input = input("Choose an option: \n")
    
        if user_Input == "a":
            print("ADD ITEM TO CART")
            itemName = input("Enter the item name: \n")
            itemDesc = input("Enter the item description: \n")
            itemPrice = float(input("Enter the item price: \n"))
            amtItem = int(input("Enter the item quantity: \n"))
            
            cart.add_item(itemName, itemPrice, amtItem, itemDesc)
            print()
            
        elif user_Input == "r":
            print("REMOVE ITEM FROM CART")
            itemToBeRemoved = input("Enter name of item to remove: \n")
            
            cart.remove_item(itemToBeRemoved)
            print()
            
        elif user_Input == "c":
            print("CHANGE ITEM QUANTITY")
            itemName = input("Enter the item name: \n")
            amtItem = int(input("Enter the new quantity: \n"))
            
            cart.modify_item(itemName, amtItem)
            print()
            
        elif user_Input == "i":
            print("OUTPUT ITEMS' DESCRIPTIONS")
            print()
            print("Item Descriptions")
            cart.print_descriptions()
            print()
            
        elif user_Input == "o":
            print("OUTPUT SHOPPING CART")
            cart.print_total()
            print()
            
        else:
            print("See ya!")
            d -= 1 
def main():
    
    c1 = ShoppingCart()
    
    c1._customerName = input("Enter customer's name: \n")
    c1._currentDate = input("Enter today's date: (Month Day, Year)\n")
    
    menu(c1)
    
main()