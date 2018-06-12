n=int(input())
temp=n
m=0
while n!=0:
	t=n%10
	m=m+t**3
	n=int(n/10)
if temp==m:
	print("yes")
else:
	print("no")
