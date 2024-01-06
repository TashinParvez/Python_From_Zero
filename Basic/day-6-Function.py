"""
-> In build Func
        int(), str(),float()
-> module Func

-> User Defined Func
"""

#------------------------> Module Func Examples
import math
# print(dir(math)) # print all math func's

from math import sqrt
# from math import *
print(sqrt(25))


#------------------------> User Defined Func

def funcName(a, b):
    print(a+b)

funcName(1,2) # call func

def sumOfTwo(a,b=2): # if b is not given the b = 2 otherwise given value for b
    print(a+b)

sumOfTwo(2,6) # call func

