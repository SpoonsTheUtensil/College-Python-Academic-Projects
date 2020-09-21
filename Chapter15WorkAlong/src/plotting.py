'''
Created on Nov 25, 2019

@author: 16368
'''

#import libraries
import turtle
import datetime

#create turtle object also open file
t = turtle.Turtle()
file = open("djia-100.txt", 'r')

decade = [1900, 1910, 1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000]

#set variables
maxDJIA = 0
startDate = datetime.datetime(1900, 1, 1)
maxDate = startDate

#loop through data to find max values and dates
for line in file:
    lst = line.split(",")
    dateStr = lst[0]
    djia = float(lst[1])
    
    year = int(dateStr[0:2]) + 1900
    month = int(dateStr[2:4])
    day = int(dateStr[4:6])
    
    date = datetime.datetime(year, month, day)
    
    if djia > maxDJIA:
        maxDJIA = djia
        
    if date > maxDate:
        maxDate = date
        
#calculate number of days to plot
dateDiff = maxDate - startDate
totalDays = dateDiff.days

#set up screen size
screen = t.getscreen()
screen.setworldcoordinates(-500, -1500, totalDays+5000, maxDJIA+1500)

t.speed(100)
t.up()
t.goto(totalDays/2, maxDJIA+500)
t.write("Decades")
t.goto(totalDays+500, (maxDJIA/2)+500)
t.write("Value")

t.goto(0, 0)
t.down()
decadeCount = 0

#draw vertical lines
for x in range(0, totalDays, int(totalDays/10)):
    t.goto(x, maxDJIA)
    t.up()
    t.write(str(decade[decadeCount]))
    decadeCount += 1
    t.goto(x+3652, 0)
    t.down()

t.goto(0, 0)
yStep = int(maxDJIA / 10)
t.up()
t.goto(0, yStep)

#draw horizontal lines
for y in range(yStep, int(maxDJIA), yStep):
    t.down()
    t.goto(totalDays, y)
    t.up()
    t.write("   $" + str(y))
    t.goto(0, y+yStep)

t.goto(0, 0)
t.speed(0)
t.pencolor("red")
t.down()

#speed up drawing and move to first record
screen.tracer(100)
file.seek(0)

for line in file:
    lst = line.split(",")
    dateStr = lst[0]
    djia = float(lst[1])
    
    year = int(dateStr[0:2]) + 1900
    month = int(dateStr[2:4])
    day = int(dateStr[4:6])
    
    date = datetime.datetime(year, month, day)
    
    dateDiff = date - startDate
    t.goto(dateDiff.days, djia)
    
screen.update()
screen.exitonclick()
file.close()
