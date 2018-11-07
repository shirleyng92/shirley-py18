# -*- coding: utf-8 -*-
"""
Created on Wed Nov  7 10:02:02 2018

@author: shirley.ng
"""

import csv
#
#myCSVFile = open("data/demo.csv","r")
#dataFromFile = csv.reader(myCSVFile)
#
#print(dataFromFile)
#
#for row in dataFromFile:
#        print(row)
#        
#myCSVFile.close()
#

fileName = "demo.csv"
accessmode = "r"

with open(fileName,accessmode) as myCSVFile:
    dataFromFile = csv.reader(myCSVFile)

    for row in dataFromFile:
        
#        #print data in set
#        print(row)
#        #print value row by row
#        for values in row:
#            print(values)
        #print data in set without brackets, set deliminter
        print(" ".join(row))
        
myCSVFile.close()