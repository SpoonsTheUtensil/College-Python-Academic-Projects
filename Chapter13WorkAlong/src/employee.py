'''
Created on Nov 11, 2019

@author: 16368
'''

from person import person

class employee(person):
    
    def __init__(self, first, last, dob, address1, city, personState, zip, empNum, dept, div):
        super().__init__(first, last, dob, address1, city, personState, zip)
        self._empNumber = empNum
        self._dept = dept
        self._div = div
        
    def __str__(self):
        return super().__str__() + "\n" + \
            "Employee Number: " + self._empNumber + "\n" + \
            "Department: " + self._dept + "\n" + \
            "Division: " + self._div + "\n"
