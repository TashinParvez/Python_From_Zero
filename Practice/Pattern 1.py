'''   
n=5
    *
   **
  ***
 ****
*****
'''



def print_pattern(num):
    for i in range(1, num+1):
        for j in range(1, num+1):
            if(j>num-i):
                print('*', end = '')
            else:
                print(' ', end = '')
        print()

num = int(input("Enter line no: ")) 
print_pattern(num)




