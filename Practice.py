#---------------------------------------------------------------- Function with Default Arguments

def printInfo(name, age='N/A', cgpa='N/A'):
  print(f'Name: {name}, Age: {age}, CGPA: {cgpa}')


printInfo("Mr.Z", 35, 3.87)
printInfo("Mr.Z", 35)
printInfo("Mr.Z")

# printInfo()
