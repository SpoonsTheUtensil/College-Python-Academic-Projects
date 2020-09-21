'''
Created on Oct 21, 2019

@author: 16368
'''

def main():
    
    start = WorkAlong()
    try:
        start.user_input()
        
    except ValueError:
        print("ValueError: Enter a float value.")
        return start.user_input()
    
    print("Weights:", start.people_Weight)
    
    print()
    start.avg_weight()
    print()
    start.max_weight()
    print()
    start.kilo_conversion()
    print()
    start.sort_weight()
    print()
    start.reverse_sort()
    print()
    
class WorkAlong:
    
    def __init__(self):
        self.people_Weight = []
        self.num_weights = 4
        
    def user_input(self):
        for i in range(self.num_weights):
            self.singleWeight = float(input("Enter weight %d: \n" % (i + 1)))
            self.people_Weight.append(self.singleWeight)
        
    def avg_weight(self):
        avgWeight = sum(self.people_Weight) / len(self.people_Weight)
        return print("Average weight: %.2f" % avgWeight)

    def max_weight(self):
        return print("Max weight: %.2f" % max(self.people_Weight))
    
    def kilo_conversion(self):
        try:
            self.index = int(input("Enter an index number: (1 - 4)\n"))
            
        except:
            if self.index < 1 or self.index > 4:
                raise "Wrong Number please enter 1 - 4"
            return self.index
        self.chosenWeight = self.people_Weight[self.index - 1]
        
        print("Weight in pounds: %.2f" % self.chosenWeight)
        print("Weight in kilograms: %.2f" % (self.chosenWeight / 2.2))

    def sort_weight(self):
        self.people_Weight.sort()
        return print("Shorted List:", self.people_Weight)
    
    def reverse_sort(self):
        self.people_Weight.sort(reverse = True)
        return print("Rev. Sorted list:", self.people_Weight)

main()    
    