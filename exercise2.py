# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 11:58:23 2018

@author: shirley.ng
"""

myFile = open("demo.csv","r")
fileContent = myFile.readline()

while fileContent:
    print(fileContent)
    fileContent = myFile.readline()

myFile.close()