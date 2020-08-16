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