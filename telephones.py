n, m = map(int, input().split())
while n != 0 or m!= 0:
    calls = []
    for _ in range(n):
        a, b, s, t = map(int, input().split())
        calls.append((s, s+t))
    calls.sort()

    for _ in range(m):
        s, t = map(int, input().split())
        count = 0
        for c in calls:
            if (s >= c[0] and s < c[1]) or (s+t > c[0] and s+t < c[1]) or (s < c[0] and s+t >= c[1]):
                count += 1
            if s+t <= c[0]:
                break
        print(count)
    n, m = map(int, input().split())
