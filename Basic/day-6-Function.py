"""
-> In build Func
        int(), str(),float()

-> module Func

-> User Defined Func
"""

#----------------------------------> Module Func Examples

import math
# print(dir(math)) # print all math func's

from math import sqrt
# from math import *
print(sqrt(25))


#-------------------------------------------------------------------> User Defined Func

def functionname(x, y):   # Have return value
  return 0


def printHello():         # Have no Return Type
  print('hello')

printHello() # Call the Func



#----------------------------------------------- Function with Default Arguments

def printInfo(name, age='N/A', cgpa='N/A'):
  print(f'Name: {name}, Age: {age}, CGPA: {cgpa}')


printInfo("Mr.Z", 35, 3.87)
printInfo("Mr.Z", 35)
printInfo("Mr.Z")

# printInfo() 



#------------------------------------------------------- Keyword/Named Arguments

def printInfo(name, age, cgpa='N/A'):
  print(f'Name: {name}, Age: {age}, CGPA: {cgpa}')


printInfo(age=35, cgpa=3.87, name="Mr.Z") 
printInfo(age=35, name="Mr.Z")

# printInfo()

