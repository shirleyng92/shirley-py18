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
import re   
#
#hand = open('data/mbox-short.txt')
#
#for line in hand:
#    line = line.rstrip()
    
    ##can get any line contain "From:"
    #if re.search('From:', line):
    
    ##only get the line start with "From:"
    #if re.search('^From:', line):
     
    #if re.search('^X.*:', line):
    
#    #^ = match from beginning of line
#    #X- text to match
#    #\S non-whitespace
#    #+ must have 1 and above
#    #: text to match
#    if re.search('^X-\S+:', line):
#
#    ##at least 1 upper case and 1 number
#    if re.search('[A-Z][0-9]+', line):

#        print(line)
    
    #print(re.findall('[0-9]+',line))
#    

##example 3
#
#x = 'My 2 favourite numbers are 7 and 25'
#y = re.findall('[0-9]+', x)
#
#print(y)

##example 4
#
#hand = open('data/mbox-short.txt')
#
#for line in hand:
#    line = line.rstrip()
#    
#        print(line)

x = 'we just received $10.00 for cookies.'

##$ is special character,put a slash to treat the special char to string
##if need to search \s, can use \\s
y = re.findall('\$[0-9.]+',x)
print(y)




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
