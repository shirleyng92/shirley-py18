# -*- coding: utf-8 -*-
"""
Created on Thu Nov 15 10:16:50 2018

@author: shirley.ng
"""
####closure
#def make_inc(x):
#    def inc(y):
#        
#        return x+y
#    return inc
#
#if __name__ == "__main__":
#    inc5 = make_inc(5)
#    inc10 = make_inc(10)
#
#print(inc5(5))
#print(inc10(5))
#
###decorater
def say_hello(name):
    return "Hello, " + str(name) + "!"

def p_decorate(func):
    def func_wrapper(name):
        return "<p>" + func(name) + "</p>"
    return func_wrapper

if __name__ == "__main__":
    my_say_hello = p_decorate(say_hello)
    print(my_say_hello("John"))
