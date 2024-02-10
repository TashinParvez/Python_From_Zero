# Palindrome Checker

'''
Write a program that checks if a given word or phrase is a palindrome. 
A palindrome is a word, phrase, number, or other sequence of characters 
that reads the same forward and backward, ignoring spaces and punctuation.
'''

word = input("Enter value: ") 

for i in range(0, len(word)):
    if(word[i] != word[int(len(word))-1-i]):
        print("NOT Palindrome")
    if(i>=len(word)//2):                 # imp integer division
        print("Palindrome")
        break

print("WORK DONE")