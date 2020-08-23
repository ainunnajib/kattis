n, l = map(int, input().split())
t = 0
last = 0
for _ in range(n):
    d, r, g = map(int, input().split())
    t += (d - last)
    cycle = r + g
    if t % cycle <= r:
        t += r - t % cycle
    last = d
t += l - last
print(t)
