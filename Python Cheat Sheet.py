a = 10 
print(f"The value of a = {a}")
print("value of a is",a , sep = " = " , end="__") 



"""
 ---> Range
 --------------------------------------------------------------------------------
 - include the first value must                   (Two parameters)
 - last limit is not included                     (one or two or three parameters)
 - if have 3rd value that increment or decrement  (three parameters)
"""



list1 = [10, 20, -6 , 90, 17, 'DHAKA', 'Jessore']
print(list1[1:3])           #------->    Print    a to b (b not included)  [List Slicing]
list1.append(85)            #--------->  insert last
list1.insert(2, 100)        #---->       insert in an index (particular index)
list1.remove(9)             #---->       Remove first found 9 [not all 9]
print(88 in list1)          #---->       check element present or Not (RETURN TRUE/FALSE)
list1.clear()               #--------->  Clear all list elements
list1.sort()                #---->       Ascending Order sort
list1.sort(reverse=True)    #---->       Desending order sort
list1 += list2              #---->       list2 added to the list1
list1.extend(list1)         #---->       Another way to add list




t1 = (1,2,3,2)       # Tuple not changeable
x, y, z, zz = t1
print(t1.count(2))   # count total occurance of 2
print(t1.index(2))   # first index of 2






student = {
    "joseph": 3.85,
    "alex": 3.2,
    "john": 3.9,
    "jane": 3.5
  #  "key" : value 
}

print(student["joseph"])      # Value Print
if "jane" in student:         # Value Exist check
  print("jane exists")

student["doe"] = 3.65         # Add element
print(student)                # print Dictionary
student.pop("jane")           # pop element 

for i in student:             #-----> Using key 
    print(i ," -> " ,  student[i])
print()

for k in student.keys():            #-----> Using keys
  print(k, '->', student[k])
print()

for k,v in student.items():            #-----> Using items 
  print(k, '->', v)
print()











