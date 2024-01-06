first = input("Enter 1st num: ")
operator = input("Enter operator (+,-,*,/,%) : ")
second = input("Enter 1st num: ")

first = int(first)
second = int(second)

if operator == '+':
    print(first + second )
elif operator == '-':
     print(first - second )
elif operator == '*':
     print(first * second )
elif operator == '/':
     print(first / second )
elif operator == '%':
     print(first % second )
else:
    print("Invalid Operator")

