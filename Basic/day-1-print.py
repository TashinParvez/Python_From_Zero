print("Hello World")

print('print("Hello World") Hello World') 
print('print("Hello World") Hello World')

answer = "TASHIN"
print(f"Name : {answer}") # advance python 
                          # [f means formated & what is with in the second bracket that will be replaced by a value of the variable]



# print ( *object , sep =" ", end="\n", . . .. . .)
a = 10
print("value =",a)
print("value",a , sep = " = ") 
print("value",a , sep = " -> ") 

print("value",a , end="\t")  
print("value",a ) 


# print without new line

print("Hello", end='>')
print("World")

print("Hello", end='')
print("World")

print("Hello", end=' ')
print("World")



## Formatting the string

# WAY 1 : (Dot format Approach)

val1,val2 = 10,20
address = "this is my road num {} and this is my house num {}".format(val1,val2)  ## {} -> will be replaced by the format values
print(address)


print("value1 = {1} , Value2 = {0}".format(val1, val2))
print("value1 = {0} , Value2 = {1}".format(val1, val2))


print("Road = {Road} , House = {House}".format(Road= val1, House= val2))
print("House = {House} , Road = {Road}".format(Road= val1, House= val2))



num = 12.10

print("formate = {:012.05f}".format(num))


'''

:12.05f   -> print er aage space dibe total 12 digit er bananor jonno   =     12.10000
   .05f   -> point er por 5 digit banabe 0 bosiye

:012.05f  -> print er aage zero  dibe total 12 char er bananor jonno   =0000012.10000
1:012.05f -> clone er aage num represent the order to get from format


'''



# WAY 2 : (f Approach)

a = 15

# "The value of a is 15"
print("The value of a is", a)  # normal print as print multiple objects 

# "The value of a = 15"
print("The value of a = {a}")   # just take as a string

print(f"The value of a = {a}")  # formate the string 

print(f"This is a+b = {a+b}")



