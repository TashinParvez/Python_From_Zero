'''
n=4
*
**
***
****
'''

def print_pattern(num):
    for i in range(1, num+1):
        for j in range(1, i+1):
                print('*', end = '') 
        print()

num = int(input("Enter line no: ")) 
print_pattern(num)
