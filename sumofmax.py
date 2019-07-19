try:
	m=int(input())
	arr=list(map(int,input().split()))
	sum=0
	a1=[]
	for i in range(0,m-1):
		if(arr[i]<arr[i+1]):
			a1.append(arr[i+1])
		else:
			a1.append(arr[i])
	for j in range(0,len(a1)):
		sum=sum+a1[j]
	print(sum)
except ValueError:
	print("invalid")
