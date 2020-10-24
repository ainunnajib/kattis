from sys import stdin, stdout
n = int(stdin.readline())
l = []
for _ in range(n):
    x, z = stdin.readline().split()
    l.append((int(x), float(z)))
l.sort()

maxc = abs((l[0][1] - l[1][1])/(l[0][0] - l[1][0]))
for i in range(n-1):
    j = i+1
    c = abs((l[i][1] - l[j][1])/(l[i][0] - l[j][0]))
    if maxc < c:
        maxc = c
stdout.write(str(maxc))
