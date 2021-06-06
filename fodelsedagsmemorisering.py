n = int(input())
d = {}
for _ in range(n):
    a, b, c = input().split()
    b = int(b)
    if c in d:
        if d[c][1] < b:
            d[c] = (a, b)
    else:
        d[c] = (a, b)
print(len(d))
for x in sorted(d.values()):
    print(x[0])