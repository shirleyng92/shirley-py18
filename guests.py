# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 10:29:00 2018

@author: shirley.ng
"""
guests = []

guest = "0"

while guest!= " ":
    guest = input("Who is attending party? If no more please put space. ")
    guests.append(guest)
    
guests.sort()

for guest in guests:
    print (guest)
    