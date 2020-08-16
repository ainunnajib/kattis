def trim0(s):
	i = 0
	while s[i:i+1] == '0':
		i += 1
	if i == len(s):
		return '0'
	return s[i:]

a = input()
b = input()
x = len(a)
y = len(b)
if x > y:
    for i in range(x-y):
        b = '0' + b
elif y > x:
    for i in range(y-x):
        a = '0' + a
p = ""
q = ""
for i in range(len(a)):
    if int(a[i:i+1]) > int(b[i:i+1]):
        p += a[i:i+1]
    elif int(b[i:i+1]) > int(a[i:i+1]):
        q += b[i:i+1]
    else:
        p += a[i:i+1]
        q += b[i:i+1]
if p == "":
    p = 'YODA'
if q == "":
    q = 'YODA'
print(trim0(p))
print(trim0(q))