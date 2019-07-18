ro1=int(input())
ro2=[]
for v in range(0,ro1):
    ro2.append(list(map(int,input().split())))
z=0
k=0
for v in range(0,ro1):
    for j in range(0,ro1):
        if ro2[v][j]==1:
            if v!=ro1-1 and ro2[v+1][j]==0:
                z=z+1
            if j!=ro1-1 and ro2[v][j+1]==0:
                z=z+1
            if v!=0 and ro2[v-1][j]==0:
                z=z+1
            if j!=0 and ro2[v][j-1]==0:
                z=z+1
            if v==0 and j==0 or v==ro1-1 and j==ro1-1  or v==0 and j==ro1-1 or v==ro1-1 and j==0 and z==2:
                k=k+1
            elif v==1 and j>0 and j<d-1 and z==3:
                k=k+1
            elif z==4:
                k=k+1
        z=0
                
print(k)
