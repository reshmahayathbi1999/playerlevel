num,k1_shift=input().split()
k1_shift=int(k1_shift)

for i in range(k1_shift):
    num=num[-1]+num[:-1]
print(num,end=' ')
