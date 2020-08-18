a = ["aa", "ii", "uu", "ee", "oo", "yy"]
n = int(input())
while n > 0:
	maxcount = -1
	maxstring = ""
	for i in range(n):
		count = 0
		s = input()
		for j in range(len(s)-1):
			if s[j:j+2] in a:
				count += 1
		if count > maxcount:
			maxcount = count
			maxstring = s
	if maxstring != "":
		print(maxstring)
	n = int(input())

## alternative answer with count() and dictionary
#n = int(input())
#while n != 0:
#    d = {}
#    maxdouble = -1
#    for _ in range(n):
#        p = input()
#        x = p.count('aa') + p.count('ii') + p.count('ee') + p.count('uu') + p.count('oo') + p.count('yy')
#        d[x] = p
#        maxdouble = max(maxdouble, x)
#    print(d[maxdouble])
#    n = int(input())
