# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 11:18:23 2018

@author: shirley.ng
"""

#example 1
#.lower change all input to lowercase
answer=input("Would you like express shipping? (yes/no) ").lower()

#indent does matter in python, it might caused error
if answer == "yes" :
    print("That will be an extra $10")
    shippingSelected = True
else:
    print("Standard Shipping selected.")
    
print("Thank you")

if(shippingSelected) :
    print("Thank you for selecting the Express shipping!!")


##example 2
#deposit = input("How much would you like to deposit? ")
#
##use float to convert to integers & decimcals
#if float(deposit) > 100 :
#    print("You get a free toaster!")
#else:
#    print("Enjoy your mug!")
#    
#print("Have a nice day")
#
##example 3 Boolean
#deposit2 = input("How much would you like to deposit? ")
#
#if float(deposit2) > 100 :
#    #set the boolean variable to True
#    freeToaster=True
#
#if freeToaster :    
#    print("You get a free toaster!")
#    
#print("Have a nice day")
