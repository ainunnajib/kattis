a = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_."
l = input().split()
while l[0] != "0":
	shift = int(l[0])
	s = l[1]
	r = s[::-1]
	result = ""
	for c in r:
		result += a[(a.index(c)+shift)%28]
	print(result)
	l = input().split()