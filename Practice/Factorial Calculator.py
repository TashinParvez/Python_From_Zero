
# **Factorial Calculator**: 
# Write a program that calculates the factorial of a given number. 
# The factorial of a non-negative integer n is the product of all positive integers less than or equal to n.


def factorial(num):  
    ans = 1
    for i in range(1, num+1):
        ans*=i
    print(f'Fact of {num} is',ans)



num = int(input("Enter terms: ")) 
factorial(num)