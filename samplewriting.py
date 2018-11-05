# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 11:35:43 2018

@author: shirley.ng
"""

filename = "Sample.txt"
accessMode = "w"

myFile = open(filename,accessMode)
myFile.write("Hi!!\n")
myFile.write("How are you?")
myFile.close()