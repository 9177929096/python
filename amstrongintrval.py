n=int(input())
m=int(input())
for i in range(n,m):
 temp=i
 s=0
 while i!=0:
 	t=i%10
 	s=s+t**3
 	i=int(i/10)
 if temp==s:
 	print(s)
