# -*- coding: utf-8 -*-
"""
Created on Thu Nov  8 10:56:59 2018

@author: shirley.ng
"""

class critter:
    
    def talk(self,msg):
        print(msg)
     
    def myName(self):
        print("I am Test")
        
        
##this example have no init value, so arguments will not in the class
crit1 = critter()
crit1.talk("Hi")


#crit1.myName()
