'''
Created on Oct 20, 2019

@author: 16368
'''

def main():
    print("Item 1")
    item1Name = input("Enter the item name: \n")
    item1Price = float(input("Enter the item price: \n"))
    item1Amt = int(input("Enter the item quantity: \n"))
    print()
    item1 = ItemToPurchase(item1Name, item1Price, item1Amt)
    
    print("Item 2")
    item2Name = input("Enter the item name: \n")
    item2Price = float(input("Enter the item price: \n"))
    item2Amt = int(input("Enter the item quantity: \n"))
    print()
    item2 = ItemToPurchase(item2Name, item2Price, item2Amt)
    
    totalItemsCost = (item1Amt * item1Price) + (item2Amt * item2Price)
    
    print("TOTAL COST")
    item1.print_item_cost()
    item2.print_item_cost()
    print()
    print("Total: $%d" % totalItemsCost)
    

class ItemToPurchase:
    
    def __init__(self, itemName = "none", itemPrice = 0, amtItem = 0, itemDesc = None):
        self._itemName = itemName
        self._itemPrice = itemPrice
        self._amtItem = amtItem
        self._itemDesc = itemDesc
        
    def print_item_cost(self):
        totalCost = (self._amtItem * self._itemPrice)
        result = print("%s %d @ $%.2f = $%d" % (self._itemName, self._amtItem, self._itemPrice, totalCost))
        return result
    
    def print_item_desc(self):
        result = print("%s: " + self._itemDesc)
        return result
    
    
    
    
    
main()