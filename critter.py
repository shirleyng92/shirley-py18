# -*- coding: utf-8 -*-
"""
Created on Thu Nov  8 10:56:59 2018

@author: shirley.ng
"""

class critter:
    
    name=""
    
    def __init__(self,name):
        self.name = name
    
    def talk(self):
        print("Hi. I'm", self.name)
        
crit = critter("Shirley")
crit.talk()
        

    