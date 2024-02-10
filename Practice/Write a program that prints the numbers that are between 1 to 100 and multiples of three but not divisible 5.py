# Write a program that prints the numbers that are between 1 to 100 and multiples of three but not divisible 5
 
for i in range(1, 100):
  if i%3==0 and i%5!=0:
    print(i, end=' ')
