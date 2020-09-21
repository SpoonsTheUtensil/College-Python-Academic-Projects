'''
Created on Oct 20, 2019

@author: 16368
'''

class Book:
    
    def __init__(self, title, author):
        self._title = title
        self._author = author
        self._patron = None
        self._waitList = []
        
    def __str__(self):
        result = "Title: " + self._title + "\n"
        result += "Author: " + self._author + "\n"
        if self._patron:
            result += "Checked out to: " + str(self._patron) + "\n"
        else:
            result += "Not checked out.\n"
            
        result += "Wait List: \n"
        for patron in self._waitList:
            result += str(patron) + "\n"
        
        return result
    
    def getTitle(self):
        return self._title
    
    def getAuthor(self):
        return self._author
    
    def getPatron(self):
        return self._patron
    
    def borrowMe(self, patron):
        if patron.getBooksOut() == patron.MAX_BOOKS_OUT:
            print("This patron cannot borrow more books.")
            return None
        elif self._patron:
            self._waitList.append(patron)
            print("This book is already checked out.")
            print("You have been added to the wait list.")
            return None
        else:
            patron.inc()
            self._patron = patron
            print("The book " + self._title + " has been checked out to " + patron._name + ".")
            return None
        
    def returnMe(self):
        self._patron.dec()
        self._patron = None
        index = 0
        
        while index < len(self._waitList):
            waitingPatron = self._waitList[index]
            result = self.borrowMe(waitingPatron)
            if result == None:
                self._waitList.pop(index)
                return "Book loaned to waiting patron, " + str(waitingPatron._name)
            index += 1
            
        return "Book returned"
            
            
            
            
            
            
            
            
            
            
            
            
        
        
        
        
        
        