t = int(input())
for i in range(t):
    p, r, f = map(int, input().split())
    y = 0
    while p <= f:
        y += 1
        p *= r
    print(y)
