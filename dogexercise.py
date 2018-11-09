# -*- coding: utf-8 -*-
"""
Created on Fri Nov  9 08:36:00 2018

@author: shirley.ng
"""

class Dog:
    
    def __init__(self,name,age):
        self.name = name
        self.age = age
#        
dog1= Dog("dog1",9)    
dog2= Dog("dog2",9)
dog3= Dog("dog3",9)  

def get_biggest_number(*args):
    return max(args)
    
print("The oldest dog is " + str(get_biggest_number(dog1.age,dog2.age,dog3.age)) + " years old")
