"""
    List
    -------------------
    - one kind of array but store any kind of data
    - 
"""

marks = [12, 33, 34]
print(marks)

marks = ["phy" , 12, "Che" , 14]
print(marks)

print(marks[0]) # perticular index value print 


print(marks[-1]) # negative index = count from reverse [and its index start from 1]
print(marks[-2])


print(marks[1:3]) # a to b (b not included)
 

array = [10 ,10 ,20 ,30 , 40]
array.append(99)  #--------->  insert last 

print(array)

array.insert(0,00) #---->  insert in an index (particular index)
array.insert(2,00)
print(array) 

array.remove(10)    #---->          Remove first found 10 [not all 10] 
print(array) 


print(88 in array) # check element present (RETURN TRUE/FALSE)
print(20 in array)


print(len(array))  # len function

i =0

# while i<len(array):
#     print(array[i], end = ' ')
#     i+=1

array.clear() # Clear all array elements 
print(array)



array = [00, 10 ,20, 25 ,30 , 40]


for num in array:
    if num == 30:
        break  # break condition
    elif num == 25:
        continue # continue condition
    else:
        print(num)






