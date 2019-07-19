l=int(input())
m=[int(i) for i in input().split(" ")]
c=1
n=c
a1=1
for i in range(l-1):
         if(m[i]==m[i+1]):
               c=c+1
               a1=c
         elif(c>n):
               a1=c
               a1=c
               c=1
print(a1)
