alpha=input()
a=list(map(int,alpha.split()))
al=input()
s=list(map(int,alpha.split()))
if len(s)==a[0]:
    if a[1] in s:
        print("Yes")
    else:
        print("No")
