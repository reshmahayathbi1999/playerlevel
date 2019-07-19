a1=int(input())
for i in range(1,a1):
    if(a1%i==0):
        c=a1//i
        if(c%2!=0):
            break
    else:
        i=i+1
print(i)a
