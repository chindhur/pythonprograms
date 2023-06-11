string = "this is python program"
count=0
for i in range(0,len(string)):
    if(string[i]!=' '):
        count=count+1
print("number of characters:"+str(count))