s = list(map(int, input().split()))
usages = s[::2]
recoveries = s[1::2]
u, r, t = [0] * 10, [0] * 10, [0] * 10

for i in range(10):
    u[i], r[i], t[i] = map(int, input().split())

currenttime = 0
for i in range(30):
    cycle = u[i%10] + r[i%10]

    #checking if overlap
    if currenttime >= t[i%10]:
        if (currenttime - t[i%10]) % cycle < u[i%10]:
            currenttime += u[i%10] - ((currenttime - t[i%10]) % cycle) #has to wait

    # now using the machine, need to check if the other guy needs to wait
    if currenttime >= t[i%10] - cycle:
        x = currenttime
        y = x + usages[i%10]
        a = ((x - t[i%10]) // cycle) * cycle + t[i%10]
        b = a + u[i%10]
        c = a + cycle
        d = c + u[i%10]

        if (a >= x and a < y) or (b > x and b <= y) or (a <= x and b >= y) \
        or (c >= x and c < y) or (d > x and d <= y) or (c <= x and c >= y):
            t[i%10] = y

    currenttime += usages[i%10] + recoveries[i%10]

currenttime -= recoveries[-1]
print(currenttime)
