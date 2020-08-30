import sys
inputs = iter(sys.stdin.readlines())
n, m = map(int, next(inputs).split())
while n + m > 0:
    a = set()
    for _ in range(n):
        a.add(int(next(inputs)))
    b = set()
    for _ in range(m):
        b.add(int(next(inputs)))
    print(len(a&b))
    n, m = map(int, next(inputs).split())
