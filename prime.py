n=int(input())
num=0
for i in range(2,(n//2)+1):
	if n%i==0:
	  num=1
	  break
if num==0:
            print("yes")
else:
	print("no"
