import random
s = 0
for m in range (1000):
	list = []
	for i in range (100):
		List =[j for j in range (1,81)]
		random.shuffle(List)
		for j in range (5):
			list.append(List.pop())
	list1 = [i for i in range (1,81)]
	random.shuffle(list1)
	list2 = []
	for i in range (4):
		list2.append(list1.pop())
	cont = 0
	while cont == 0:
		list2.append(list1.pop())
		mikos = len(list2)
		c = 1
		p = 0
		l = 1
		k = 0
		for j in range (500):
			if c == 5:
				c = 0
				l = l + 1
				p = 0
			for k in range (mikos):
				if list[j] == list2[k]:
					p = p + 1
			if p == 5:
				player = 1
				cont = 1
			c = c + 1
		k = k + 1
	s = s + k
print player
sum = s/1000
print sum 	
				