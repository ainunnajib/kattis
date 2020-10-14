k = int(input())
s = list(map(int, input().split()))
d = {}
while s[0] != -1:
    for x in s[1:]:
        d[x] = s[0]
    s = list(map(int, input().split()))

x = d[k]
l = [str(k), str(x)]
while x in d:
    x = d[x]
    l.append(str(x))

print(' '.join(l))
