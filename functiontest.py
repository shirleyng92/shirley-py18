# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 11:02:30 2018

@author: shirley.ng
"""

##1. Create a function to print hello
#def sayHello(firstName,lastName):
#    print("Hello "+firstName +" "+ lastName + ", how are you?")
#    return
#
##2. Invoke a function
#sayHello("Shirley"," ")
#sayHello("MY", " ")
#sayHello("SC", " ")

###example1
#def addTwo(var1,var2):
#    sum = var1+var2
#    return sum
#
#print("Sum of 5+5 = " + str(addTwo(5,5)))

##example 2
def printinfo(name,age="NULL", location="KL"):
    "This prints a passed info into this function"
    print("Name: ", name)
    print("Age: ", age)
    print("Location: ", location)
    return;

#now you can call printinfo function
printinfo("miki",50,"Penang")
printinfo(age=50, name="miki",location="PJ")
printinfo(name = "mini",location="JB")