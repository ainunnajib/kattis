n, p = map(int, input().split())
c = sorted(list(map(int, input().split())))

shift = max(p, c[0]) - c[0]
for i in range(1, n):
    shift = max(shift, max(p*(i+1), c[i]) - c[i])

print(shift + c[0])
