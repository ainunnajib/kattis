import sys
n = int(input())
r = [0 for i in range(n)]
c = [0 for i in range(n)]
s = [0 for i in range(2*n-1)]
b = [0 for i in range(2*n-1)]
for line in sys.stdin.readlines():
    x, y = map(int, line.split())
    r[y] += 1
    c[x] += 1
    z = x + y
    s[z] += 1
    z = (n-x-1) + y
    b[z] += 1
if min(r) == max(r) and min(r) == 1 and min(c) == max(c) and min(c) == 1 and max(s) == 1 and max(b) == 1:
    print('CORRECT')
else:
    print('INCORRECT')
