# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 11:18:23 2018

@author: shirley.ng
"""

#.lower change all input to lowercase
answer=input("Would you like express shipping? (yes/no) ").lower()

#indent does matter in python, it might caused error
if answer == "yes" :
    print("That will be an extra $10")
    
print("Thank you")

#example 2
deposit = input("How much would you like to deposit?")

#use float to convert to integers & decimcals
if float(deposit) > 100 :
    print("You get a free toaster!")
    
print("Have a nice day")