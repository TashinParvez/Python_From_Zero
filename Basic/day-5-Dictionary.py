marks = {"eng" : 84 , "math" : 90, "Che" : 95}

print(marks["math"])
print()

marks["phy"] = 80

marks["eng"] = 88

for i in marks:
    print(i + " -> " + str(marks[i]))