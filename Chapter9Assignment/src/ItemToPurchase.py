'''
Created on Oct 20, 2019

@author: 16368
'''

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
        result = print("%s: %s" % (self._itemName, self._itemDesc))
        return result
    
    def getItem(self):
        return self._itemName
    
    def getItemPrice(self):
        if self._amtItem > 1:
            totalCost = self._itemPrice * self._amtItem
            return totalCost
        else:
            return self._itemPrice
    
    def getAmtItem(self):
        return self._amtItem
    
    def getItemDesc(self):
        return self.print_item_desc()
    