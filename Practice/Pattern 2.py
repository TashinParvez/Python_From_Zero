'''
---------> Pattern 2.py
n = 5
*********
*******
*****
***
*
'''

def print_pattern(num):
    for i in range(num, 0, -1):
        for j in range(1, (i*2)):
                print('*', end = '') 
        print()

num = int(input("Enter line no: ")) 
print_pattern(num)