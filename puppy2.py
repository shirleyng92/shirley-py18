# -*- coding: utf-8 -*-
"""
Created on Thu Nov  8 11:27:43 2018

@author: shirley.ng
"""

class Puppy(object):
    def __init__(self):
        self.name = []
        self.color = []
        
    def __setitem__(self,name,color):
        self.name.append(name)
        self.color.append(color)
        
    def __getitem__(self,name):
        if name in self.name:
            return self.color[self.name.index(name)]
        else:
            return None
        
    def testStatic():
        print("Hi!I'm static")
        
    testStatic = staticmethod(testStatic)
        
dog = Puppy()
dog['Max'] = 'brown'
dog['Ruby'] = 'yellow'

##setitem, getitem
print("Max is", dog['Max'])

##static method
print(Puppy.testStatic())
