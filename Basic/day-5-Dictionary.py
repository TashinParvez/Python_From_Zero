marks = {
    "eng" : 84, 
    "math" : 90, 
    "Che" : 95
   # Key : value
}

print(marks["math"])
print()


marks["phy"] = 80 
marks["eng"] = 88


for i in marks:
    print(i ," -> " ,  marks[i])
print()


for k in marks.keys():
    print(k,'->',marks[k])
print()

marks.pop('phy')


for k,v in marks.items():
    print(k,'->',v) 
print()

#---------------> 

if('phy' in marks.keys()):
    print("YES")
else:
    print("NO") 
