n = int(input())
l = []
for r in range(n):
    s = input()
    for c in range(n):
        if s[c] != '.':
            l.append((r, c))
count = 0
n = len(l)
for i in range(n):
    a = l[i]
    for j in range(i+1, n):
        b = l[j]
        for k in range(j+1, n):
            c = l[k]
            if (a[0]-b[0]) * (c[1]-b[1]) == (c[0]-b[0]) * (a[1]-b[1]):
                count += 1
print(count)
