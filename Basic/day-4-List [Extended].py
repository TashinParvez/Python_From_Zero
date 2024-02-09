##------------------------------------------------------------------------ Print List


list1 = [10, 20, -6 , 90, 17, 'DHAKA', 'Jessore']


print('len of the list is', len(list1)) #------------ Print length of the List
print()

print(list1) 
print()

print("Capital of BD is", list1[5]) #-----------     Print any particular index

print(list1[-1]) #--------  negative index = count from reverse [and its index start from 1]
print()


print(list1[1:3]) #----------------------      Print    a to b (b not included)  [List Slicing]
print()


for i in range(len(list1)):   #--------------------- print list using for loops   [WAY 1] 
  print(list1[i], end=' ') 

print()



for itr in list1:             #------------------ print list using for each loops   [WAY 2] 
  print(itr , end = ' ') 

print()



i =0
while i<len(list1):         #--------------------- print list using while loops 
    print(list1[i], end = ' ')
    i+=1
print()




##---------------------------------- Insert element into the List + Remove element into the List + check element Present + Clear list elements


list1 = [10, 20, -5, 9, 9, 0]

list1.append(85)     #--------->   insert last 
print(list1)

list1.insert(2, 100)    #---->     insert in an index (particular index)
print(list1)

list1.remove(9)    #---->          Remove first found 9 [not all 9] 
print(list1)


print(88 in list1)   #---->        check element present or Not (RETURN TRUE/FALSE)
print(list1)



list1.clear()           #--------->              Clear all list elements 
print(list1)


##---------------------------------------------------------------- List Slicing (take a part from the list)

list1 = [10, 20, 100, -5, 9, 0, 85]

newlist = list1[2:6] # slicing [last index is not included]  

print(newlist)


##------------------------------------------------------------------------ Sort List

list1 = [10, 20, 100, -5, 9, 0, 85]

list1.sort()  # Ascending Order sort
print(list1)


list1.sort(reverse=True) # Desending order sort
print(list1)


##------------------------------------------------------------------------- ADD List

list1 = [10, 11, -5]
list2 = [5, -6, 1]

print(list1)

list1 += list2    # list2 added to the list1

print(list1)  


list3 = [10, 11, -5]
list4 = [5, -6, 1]

list3.extend(list4)  # Another way to add list  

print(list3)  


