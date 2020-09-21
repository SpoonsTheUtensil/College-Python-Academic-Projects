'''
Created on Nov 11, 2019

@author: 16368
'''

from person import person

class student(person):
    
    def __init__(self, first, last, dob, address1, city, personState, zip, major, minor, gpa, grade):
        super().__init__(first, last, dob, address1, city, personState, zip)
        self._major = major
        self._minor = minor
        self._gpa = gpa
        self._grade = grade
        
    def __str__(self):
        return super().__str__() + "\n" + \
            "Major: " + self._major + "\n" + \
            "Minor: " + self._minor + "\n" + \
            "GPA: " + self._gpa + "\n" + \
            "Student Year: " + self._grade + "\n"