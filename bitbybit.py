def opand(a, b):
	if a == '0' or b == '0':
		return '0'
	if a == '1' and b == '1':
		return '1'
	return '?'
def opor(a, b):
	if a == '1' or b == '1':
		return '1'
	if a == '0' and b == '0':
		return '0'
	return '?'

n = int(input())
while n > 0:
	s = ['?' for x in range(32)]
	for i in range(n):
		l = input().split()
		if l[0] == "SET":
			s[int(l[1])] = '1'
		elif l[0] == "CLEAR":
			s[int(l[1])] = '0'
		elif l[0] == "AND":
			s[int(l[1])] = opand(s[int(l[1])], s[int(l[2])])
		elif l[0] == "OR":
			s[int(l[1])] = opor(s[int(l[1])], s[int(l[2])])
	print(''.join(s[::-1]))
	n = int(input())