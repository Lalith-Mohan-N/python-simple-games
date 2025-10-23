from random import *
import calendar

Name = input("Enter your name : ")
year = int(input("Enter your Birth year : "))
Month = int(input("Enter your Birth Month : "))
date = int(input("Enter your birth DATE : "))

print("Hello ",Name,"  Welcome to PYTHON ASTROLOGER !")
print("Good to se you")

print(calendar.month(year,Month))
print("HELLO ! ",Name," your DOB is :",Month,"-",date,"-",year)
r1=randint(60,80)
r2=randint(20,30)

print(Name,"You will get Married by ",r2,"Years")
print(Name,"You will die by",r1,"Years  Enjoy your life... ! \n THANKS BUDDY  ! ")
print(calendar.calendar(year))
