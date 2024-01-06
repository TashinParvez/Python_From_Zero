marks = [12, 33, 34]
print(marks)

marks = ["phy" , 12, "Che" , 14]
print(marks)
print(marks[0]) # perticular index value print
print(marks[2])

print(marks[-1]) # neg index = count from reverse
print(marks[-2])

print(marks[1:3]) # a to b (b not included)
 

array = [10 ,20 ,30 , 40]
array.append(99)  # insert last

print(array)

array.insert(0,00) # insert in an index
array.insert(2,00) # insert in an index
print(array) 

print(88 in array) # check element present
print(20 in array)


print(len(array))  # len function

i =0

# while i<len(array):
#     print(array[i])
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






