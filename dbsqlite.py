# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 10:33:46 2018

@author: shirley.ng
"""

import sqlite3 as lite
import sys

con = None
try:
    #con = lite.connect('newtest.db')
    
    con = lite.connect('testdb.db')
    cur = con.cursor()
    
    #cur.execute('SELECT SQLITE_VERSION()')
    cur.execute('Select * from stuff')
    
    ''''''''''''''''''''''''''''''''''''''''
    ##fetching 1 data only
    data = cur.fetchone()
    print(f'SQLite version: {data}')
    ''''''''''''''''''''''''''''''''''''''''
    
except lite.Error as e :
    print(f"Error {e.args[0]}")
finally :
    if con:
        con.close()