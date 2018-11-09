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
dog1= Dog("dog5",11)    
dog2= Dog("dog2",12)
dog3= Dog("dog3",11)  

def get_biggest_number(*abc):
    return max(abc)
    
print("The oldest dog is " + str(get_biggest_number(dog1.age,dog2.age,dog3.age)) + " years old")

#another way to print
print("The oldest dog is {} years old".format(get_biggest_number(dog1.age,dog2.age,dog3.age)))
print(f"The oldest dog is {get_biggest_number(dog1.age,dog2.age,dog3.age)} years old")
