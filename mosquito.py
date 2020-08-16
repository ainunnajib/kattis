import sys
for line in sys.stdin.readlines():
    m, p, l, e, r, s, n = map(int, line.split())
    for _ in range(n):
        lnext = m*e
        m = int(p/s)
        p = int(l/r)
        l = lnext
    print(m)
