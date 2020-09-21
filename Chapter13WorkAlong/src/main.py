'''
Created on Nov 11, 2019

@author: 16368
'''

from person import person
from employee import employee

def main():
    emp1 = person("Jennifer", "Jones", "4/6/1964", "4601 Mid Rivers Mall Dr.", "Cottleville", "MO", "63376")
    emp2 = employee("Rex", "McKanry", "1/1/1900", "4602 River Dr.", "St. Peters", "MO", "63366", "1007", "Computer Science", "Engineering and Technology")

    print(emp1)
    print(emp2)
    
main()
