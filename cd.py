import sys
inputs = iter(sys.stdin.readlines())
n, m = map(int, next(inputs).split())
while n + m > 0:
    d = []
    for _ in range(n):
        d.append(int(next(inputs)))
    count = 0
    i = 0
    for _ in range(m):
        x = int(next(inputs))
        if i >= n:
            continue
        if d[i] == x:
            count += 1
            i += 1
        elif d[i] < x:
            while d[i] < x:
                i += 1
                if i >= n:
                    break
            if i < n:
                if d[i] == x:
                    count += 1
                    i += 1
    print(count)
    n, m = map(int, next(inputs).split())
