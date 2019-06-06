'''
    Author: Jay Lee
    Date: 05/06/19
    Version: 1.0
    Purpose: to find out possible options for taeyoung 
    to reach his current lp

*'''
import math

#VARIABLES
currentLP = int(input("Please Enter your current LP Taeyoung:"))#get userinput for current LP Taeyoung is at
gain = 15
lose = -14      
keepGoing = True #boolean value to keep iterating through the while loop
count = 1
progress = 0 #current lp going through the loop
numOfWin = 0
numOfLoss = 0

while(keepGoing):
    if progress < currentLP:
        progress += gain
        print("{:4} | {:4} | {:4}".format(count, progress, "w"))
        count += 129
        numOfWin += 1
    elif progress > currentLP:
        progress += lose
        print("{:4} | {:4} | {:4}".format(count, progress, "l"))
        numOfLoss += 1
        count += 1
    elif progress == currentLP:
        print("It took {} wins and {} losses".format(numOfWin, numOfLoss))
        keepGoing = False