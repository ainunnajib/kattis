# submit this into Kattis as Python 2 instead of Python 3
# Python 3 = TLE, Python 2 = AC
import sys
inputs = iter(sys.stdin.readlines())
n, m = map(int, next(inputs).split())
while n + m > 0:
    a = set()
    for _ in range(n):
        a.add(next(inputs))
    b = set()
    for _ in range(m):
        b.add(next(inputs))
    print(len(a&b))
    n, m = map(int, next(inputs).split())
