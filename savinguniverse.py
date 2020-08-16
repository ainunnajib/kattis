from collections import defaultdict
n = int(input())
for i in range(1, n+1):
	result = 0
	k = int(input())
	d = defaultdict(int)
	for j in range(k):
		d[input()] = 0
	x = d.copy()
	k = int(input())
	for j in range(k):
		s = input()
		x[s] += 1
		if(min(x.values()) > 0):
			result += 1
			x = d.copy()
			x[s] += 1
	print("Case #" + str(i) + ": " + str(result))