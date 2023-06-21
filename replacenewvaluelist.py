#to find an element in list and replace with new value if found
list=list(map(int,input().split()))
print(list)
old_value=int(input("enter old value :"))
new_value=int(input("enter new value :"))
if old_value in list:
    index=list.index(old_value)
    list[index]=new_value
print(list)