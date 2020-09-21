'''
Created on Oct 20, 2019

@author: 16368
'''

from Patron import Patron
from Book import Book

def main():
    p1 = Patron("Jeff")
    p2 = Patron("Jill")
    
    b1 = Book("Atonement", "McEwan")
    b2 = Book("The March", "Doctorow")
    b3 = Book("Beach Music", "Conroy")
    b4 = Book("Thirteenth Moon", "Frazier")
    
    print(p1)
    print(p2)
    
    print(b1)
    
    b1.borrowMe(p1)
    b2.borrowMe(p1)
    b3.borrowMe(p1)
    
    b1.borrowMe(p2)
    print(b1)
    
    print(b1.returnMe())
    b4.borrowMe(p1)
    b4.borrowMe(p1)
    
    print(p1)
    print(p2)
    
    print(b1)
    print(b2)
    print(b3)
    print(b4)
    
main()
