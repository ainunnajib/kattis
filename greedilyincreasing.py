n = int(input())
a = list(map(int, input().split()))
g = [str(a[0])]
c = a[0]
for x in a:
    if x > c:
        c = x
        g.append(str(x))
print(len(g))
print(' '.join(g))
