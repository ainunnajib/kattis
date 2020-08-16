n = int(input())
a = []
for i in range(n):
	s = input()
	l = s.split()
	if l[0] not in a:
		a.append(l[0])
		print(s)
	if len(a) == 12:
	    break