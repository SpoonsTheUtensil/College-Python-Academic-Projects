'''
Created on Nov 4, 2019

@author: 16368
'''

# Get file Name
fileName = input("Enter the file name: ")

# Open payroll file
inputFile = open(fileName, 'r')

# Create output file
outputFile = open("payroll.txt", 'a')

# Set title and read from file
print("%-15s%6s%15s%12s" % ("Name", "Hours", "Hourly Rate", "Total Pay"))
outputFile.write("%-15s%6s%15s%12s\n" % ("Name", "Hours", "Hourly Rate", "Total Pay"))

for line in inputFile:
    dataList = line.split()
    name = dataList[0]
    hours = float(dataList[1])
    payRate = float(dataList[2])
    
    totalPay = hours * payRate
    print("%-15s%6.2f%15.2f%12.2f" % (name, hours, payRate, totalPay))
    outputFile.write("%-15s%6.2f%15.2f%12.2f\n" % (name, hours, payRate, totalPay))

outputFile.close()
