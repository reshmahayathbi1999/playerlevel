p=int(input())
coun=0
for i in range(p):
        q,r=map(int,input().split(" "))
        if(q<r):
             coun=coun+1
print(coun)
