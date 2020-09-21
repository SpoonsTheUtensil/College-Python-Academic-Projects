'''
Created on Oct 20, 2019

@author: 16368
'''

class Patron:
    MAX_BOOKS_OUT = 3
    
    def __init__(self, name):
        self._name = name
        self._numBooksOut = 0
        
    def __str__(self):
        result = self._name + ", " + str(self._numBooksOut) + \
            " books out."
        return result
    
    def getName(self):
        return self._name
        
    def getBooksOut(self):
        return self._numBooksOut
        
    def inc(self):
        self._numBooksOut += 1
        
    def dec(self):
        self._numBooksOut -= 1
