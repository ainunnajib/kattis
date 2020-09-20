n, p, k = map(int, input().split())
tt = list(map(int, input().split()))
time = 0
cur = 0
perc = 100.0
for t in tt:
    time += (t-cur)*perc/100.0
    perc += p
    cur = t
time += (k-cur)*perc/100.0
print(time)
