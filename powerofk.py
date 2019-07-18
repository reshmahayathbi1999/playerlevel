l,m=map(int,input().split(" "))
flagg=0
for i in range(1,l):
         if(m**i==l):
               flagg=1
               break
if(flagg==1):
       print("yes")
else:
       print("no")
