list=[(78,89,45),(56,78,43),(6,8,9)]
replace=input("enter item to replace:")
new_list = [(*t[:-1], replace) for t in list]
print(new_list)