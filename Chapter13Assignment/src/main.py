'''
Created on Nov 11, 2019

@author: 16368
'''

from person import person
from employee import employee
from student import student

def main():
    emp1 = person("Jennifer", "Jones", "4/6/1964", "4601 Mid Rivers Mall Dr.", "Cottleville", "MO", "63376")
    emp2 = employee("Rex", "McKanry", "1/1/1900", "4602 River Dr.", "St. Peters", "MO", "63366", "1007", "Computer Science", "Engineering and Technology")

    student1 = person("John", "Smith", "1/24/1990", "4603 Mid Ribbit Lane", "St. Charles", "MO", "63309")
    student2 = student("Jonah", "Smiles", "10/31/1990", "1409 Skeleton Key Road", "Lake St. Louis", "MO", "63313", "Computer Science", "Cybersecurity", "4.0", "Senior")
    student3 = employee("Jimmy", "Neutron", "12/31/1999", "13 Neutron Lane", "St. Einstein Ave.", "MO", "63078", "1313", "Science", "Chemistry")

    print(emp1)
    print(emp2)
    print(student1)
    print(student2)
    print(student3)
    
main()
