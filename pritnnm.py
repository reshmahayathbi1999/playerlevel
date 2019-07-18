n=int(input())
s=str(input())
a1=""
r=""
for i in range(len(s)):
    if s[i]=='1':
        a1=a1+s[i]+" "
    elif s[i]=='0':
        r=r+a1
        a1=""
print(r.strip())
