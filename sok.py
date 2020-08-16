s = input().split()
a = [ int(x) for x in s ]
s = input().split()
r = [ int(x) for x in s ]
z = [ 1.0*a[i]/r[i] for i in range(3) ]
minz = min(z)
result = ""
for i in range(3):
    if i > 0:
        result += ' '
    result += str(a[i]-minz*r[i])
print(result)