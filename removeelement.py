#Write a Python program to print a specified list after removing the 0th, 4th and 5th elements.

list=[34,56,32,12,45,67,43,23]

list=[x for(i,x) in enumerate(list) if i not in (0,4,5)]

print(list)
