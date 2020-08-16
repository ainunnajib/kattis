a = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
s = input()
l = len(s)
h = int(l/2)
s1 = s[:h]
s2 = s[h:]
total = 0
for c in s1:
    total += a.index(c)
r1 = ""
for c in s1:
    r1 += a[(a.index(c)+total)%26]
total = 0
for c in s2:
    total += a.index(c)
r2 = ""
for c in s2:
    r2 += a[(a.index(c)+total)%26]
r = ""
for i in range(h):
    r += a[(a.index(r1[i])+a.index(r2[i]))%26]
print(r)