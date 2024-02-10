
# **Prime Number Checker**: 
# Write a program that checks if a given number is prime. 
# A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.



def is_prime(num):   
    if(num <=2 ):
        print("Prime")
        return
    else:
        for i in range(2, num//2):
            if(num%i == 0):
                print("Not Prime")
                return
        print("prime")
        



num = int(input("Enter terms: ")) 
is_prime(num)