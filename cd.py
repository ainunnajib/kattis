import sys
inputs = iter(sys.stdin.readlines())
n, m = map(int, next(inputs).split())
while n + m > 0:
    d = {}
    for _ in range(n):
        d[int(next(inputs))] = 1
    count = 0
    for _ in range(m):
        if int(next(inputs)) in d:
            count += 1
    print(count)
    n, m = map(int, next(inputs).split())
