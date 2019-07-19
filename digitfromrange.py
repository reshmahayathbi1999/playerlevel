s,a1=map(str,input().split())
f1=0
a=int(a1)
s=list(s)
for i in range(a+1):
    if(str(i) in s):
        f1=1
        continue
    else:
        f1=0
        break
if(f1==1):
    print("yes")
else:
    print("no")
