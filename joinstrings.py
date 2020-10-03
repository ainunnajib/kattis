import sys

inputs = iter(sys.stdin.readlines())
n = int(next(inputs))
l = ['']
d = {}
x = {}

for _ in range(n):
    l.append(next(inputs).strip())

a, b = 1, 1
for _ in range(n-1):
    a, b = map(int, next(inputs).split())
    if a not in x:
        x[a] = a
    if b not in x:
        x[b] = b

    d[x[a]] = b
    x[a] = x[b]

print(l[a], end = '')
while a in d:
    a = d[a]
    print(l[a], end = '')
