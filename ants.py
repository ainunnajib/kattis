t = int(input())
for _ in range(t):
    l, n = map(int, input().split())
    d = []
    while len(d) < n:
        d.extend(list(map(int, input().split())))

    a, b = 0, 0
    for x in d:
        a = max(a, min(x, l-x))
        b = max(b, max(x, l-x))

    print(a, b)
