list=[45,34,12,11,65,30,17]
list.sort()
length=len(list)
print("largest is:",list[length-1])
print("smallest is:",list[0])
print("second largest:",list[length-2])
print("second smallest:",list[1])


#using max and min
list=[34,56,78,21,18]
smallest=min(list)
print(smallest)
largest=max(list)
print(largest)
list.remove(smallest)
print("second smallest",min(list))
list.remove((largest))
print("second largest",max(list))
