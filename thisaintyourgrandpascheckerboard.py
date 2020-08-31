n = int(input())
fail = False
a = []
for _ in range(n):
    a.append([c == 'W' for c in input()])
for j in range(n):
    if sum(a[j]) != n//2:
        fail = True
    for i in range(n-2):
        if sum(a[j][i:i+3]) in [0, 3]:
            fail = True
for i in range(n):
    if sum([a[j][i] for j in range(n)]) != n//2:
        fail = True
    for j in range(n-2):
        if (a[j][i] + a[j+1][i] + a[j+2][i]) in [0, 3]:
            fail = True
print(1-int(fail))
