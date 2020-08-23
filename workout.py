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
        if (currenttime - t[i%10]) % cycle <= u[i%10]:
            currenttime += u[i%10] - ((currenttime - t[i%10]) % cycle) #has to wait

    # now using the machine, need to check if the other guy needs to wait
    endtime = currenttime + usages[i%10]
    if currenttime > t[i%10]: #other started before
        t[i%10] = currenttime - (currenttime - t[i%10]) % cycle
        if (t[i%10] + cycle < endtime): # other has to wait
            t[i%10] = endtime
    else: # other starts only after now
        if t[i%10] < endtime: # other has to wait
            t[i%10] = endtime

    currenttime += usages[i%10] + recoveries[i%10]

currenttime -= recoveries[-1]
print(currenttime)
