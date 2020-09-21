'''
Created on Nov 11, 2019

@author: 16368
'''

class person:
    
    def __init__(self, firstname, lastname, dob, address1, city, personState, zip):
        self._firstname = firstname
        self._lastname = lastname
        self._dob = dob
        self._address1 = address1
        self._city = city
        self._state = personState
        self._zip = zip

    def __str__(self):
        return "Name: " + self._lastname + ", " + self._firstname + "\n" + \
            "DOB: " + self._dob + "\n" + \
            "Address: " + self._address1 + "\n" + \
            "City: " + self._city + "\n" + \
            "State: " + self._state + "\n" + \
            "Zipcode: " + self._zip + "\n"