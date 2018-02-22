import random
a=[i for i in range(-30,31)]
print (a[:])
b = []
a [0:60]
b = random.sample(a,30)
print (b[:])
m=0
for j in range (0,28):
	for i in range (1,29):
		if  (b[j] + b[i] + b[i+1])==0:
			m = m + 1
			print b[j] , b[i] , b[i+1]
if m==0:
	print ("den yparxei tetoios sindiasmos")
