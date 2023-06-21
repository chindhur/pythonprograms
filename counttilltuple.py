#count the elements of tuple until find a tuple

list=[7,4,1,(6,8,9)]
count1=0
index=0
while index<len(list):
    if type(list[index]==tuple):
        break
    count1+=1
    index+=1
print(count1)