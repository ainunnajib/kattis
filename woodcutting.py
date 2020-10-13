t = int(input())
for _ in range(t):
    n = int(input())
    l = []
    for __ in range(n):
        l.append(sum(list(map(int, input().split()))[1:]))

    l.sort()
    total = 0
    cur = 0
    for x in l:
        cur += x
        total += cur

    print(total / n)
