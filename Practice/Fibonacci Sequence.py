# **Fibonacci Sequence**: 
# Write a program that generates the Fibonacci sequence up to a specified number of terms. 
# The Fibonacci sequence starts with 0 and 1, and each subsequent number is the sum of the previous two.


def fib(index):
    a = 0
    b = 1
    for i in range(0, index):
        if(i==0):
            print(a,end=' ')
        elif i==1:
            print(b,end=' ')
        else:
            print(a + b, end=' ')
            b = a+b
            a = b-a 



index = int(input("Enter terms: "))

fib(index)
