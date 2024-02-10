# Make a ft__in to m conversion calculator.py

def f_to_m(feet , inchs):
    return feet*0.3048 + inchs*0.0254


print("Meter: ", f_to_m(int(input("Enter feet: ")),int(input("Enter inchs: ")))) 