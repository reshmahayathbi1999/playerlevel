p=int(input())
for j in range(2,p):
    if(p%j==0):
        print("yes")
        break
else:
    print("no")
