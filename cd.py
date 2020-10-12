import sys
n, m = map(int, sys.stdin.readline().split())
while n + m > 0:
    a = set()
    for _ in range(n):
        a.add(int(sys.stdin.readline()))

    count = 0
    for _ in range(m):
        if int(sys.stdin.readline()) in a:
            count += 1

    print(count)

    n, m = map(int, sys.stdin.readline().split())
