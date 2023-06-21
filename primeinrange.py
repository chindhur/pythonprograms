m=int(input("enter start range: "))
n = int(input("enter end range: "))

if(m>n):
    print(-1)
flag=False
for i in range(m,n+1):
    for j in range(2,i):
        if(i%j == 0):
            break
    else:
        print(i,end=" ")
        flag = True
if(flag==False):
    print(-1)

