'''
Created on Oct 20, 2019

@author: 16368
'''

from ItemToPurchase import ItemToPurchase

class ShoppingCart:
    
    def __init__(self, customerName = None, currentDate = "January 1, 2016"):
        self._customerName = customerName
        self._currentDate = currentDate
        self._cart_items = []
        
    def add_item(self,itemName, itemPrice, amtItem, itemDesc):
        item = ItemToPurchase(itemName, itemPrice, amtItem, itemDesc)
        self._cart_items.append(item)
        
    def remove_item(self, itemName):
        for item in self._cart_items:
            if item._itemName == itemName:
                self._cart_items.remove(item)
                break
        else:
            print("Item not found in cart. Nothing removed.")
        
    def modify_item(self, itemName, itemAmount):
        for item in self._cart_items:
            if item._itemName == itemName:
                item._amtItem = itemAmount
                break
            else:
                print("Item not found in cart. Nothing modified.")
                  
    def get_num_items_in_cart(self):
        return len(self._cart_items)
        
    def get_cost_of_cart(self):
        result = 0
        for item in self._cart_items:
            result += (item._itemPrice * item._amtItem)
        return result
        
    def print_total(self):
        print("%s's Shopping Cart - %s" % (self._customerName, self._currentDate))
        if self._cart_items == []:
            print("SHOPPING CART IS EMPTY")
        else:
            print("Number of Items: %d" % len(self._cart_items))
            print()
            for item in self._cart_items:
                item.print_item_cost()
        print("Total: $%d" % self.get_cost_of_cart())
        
    def print_descriptions(self):
        print("%s's Shopping Cart - %s" % (self._customerName, self._currentDate))
        for item in self._cart_items:
            item.getItemDesc()
        
