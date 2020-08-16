s = input().split()
l = [ int(x) for x in s ]
l.sort()
s = input()
r = []
for c in s:
    if c == 'A':
        r.append(str(l[0]))
    elif c == 'B':
        r.append(str(l[1]))
    elif c == 'C':
        r.append(str(l[2]))
print(r[0]+" "+r[1]+" "+r[2])