numbers = range(5) # 0 1 2 3 4
numbers2 = range(1, 5) # 1 2 3 4

print(numbers) 
print(numbers[2])
print(numbers[4])



"""
 Range
 --------------
 - include the first value must                   (Two parameters)
 - last limit is not included                     (one or two or three parameters)
 - if have 3rd value that increment or decrement  (three parameters)
"""




for i in range(5):  # 0 to 4  (5 not included)
  print(i)

print()


# for(int i=4; i<10; ++i)
for i in range(4, 10):  # 4 to 10  (10 not included)
  print(i, end=' ')

print()
print()


# for(int i=0; i<20; i+=2)
for i in range(0, 20, 2): # 4 to 10  (10 not included)  +  increment by 2
  print(i, end=' ')

print()
print()



# for(int i=20; i>12; --i)
for i in range(20, 12, -1):  # same as before , just decrement by 1
  print(i, end=' ')

print()
print()