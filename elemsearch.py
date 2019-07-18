x1,y1=map(int,input().split())
ab=list(map(int,input().split()[:x1]))
if y1 in ab:
    print('Yes')
else:
    print('No')
