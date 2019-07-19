sp1=int(input())
arr1=[]
for i in range(sp1):
	s=input()
	s=list(map(int,s.split(" ")))
	l=len(s)
	for j in range(l):
		arr1.append(s[j])
arr1.sort()
print(*arr1,sep=" ")	
