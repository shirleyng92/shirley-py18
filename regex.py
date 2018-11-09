# -*- coding: utf-8 -*-
"""
Created on Fri Nov  9 10:45:35 2018

@author: shirley.ng
"""
##example 1
#hand = open('data/mbox-short.txt')
#
#for line in hand:
#    line = line.rstrip()
#    if line.find('From:') >= 0:
#        print(line)


###example2 using regex
#import re   
#
#hand = open('data/mbox-short.txt')
#
#for line in hand:
#    line = line.rstrip()
#    
#    ##can get any line contain "From:"
#    #if re.search('From:', line):
#    
#    ##only get the line start with "From:"
#    #if re.search('^From:', line):
#     
#    #if re.search('^X.*:', line):
#    
##    #^ = match from beginning of line
##    #X- text to match
##    #\S non-whitespace
##    #+ must have 1 and above
##    #: text to match
##    if re.search('^X-\S+:', line):
#
##        print(line)
#    
#    #print(re.findall('[0-9]+',line))
#    

##example 3
#import re
#
#x = 'My 2 favourite numbers are 7 and 25'
#y = re.findall('[0-9]+', x)
#
#print(y)

#example 4
import re

hand = open('data/mbox-short.txt')

for line in hand:
    line = line.rstrip()
    
    if re.search('[A-Z]+[0-9]+', line):
        print(line)
    





# =============================================================================
# ##shirley testing
# import re
# 
# element = open('testextract.txt')
# 
# for line in element:
#     line = line.rstrip()
#     
#     if re.search('<dt><a href=', line):
#         print(line)
# =============================================================================
