num1=int(input())
arr=[list(map(int,input().split(" "))) for i in range(num1)]
i,j=0,len(arr)-1
a,b=1,1
while i<len(arr):
    a*=arr[i][i]
    b*=arr[i][j]
    i+=1
    j-=1
print(a+b)
