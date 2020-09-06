import sys
s, n, m = map(int, input().split())
a = []
for line in sys.stdin.readlines():
    a += list(map(int, line.split()))
inc, dec, peak, valley = 0, 0, 0, 0
hike, slope = False, False
for i in range(s-1):
    if a[i+1] > a[i]:
        dec = 0
        hike = False
        inc += 1
        if inc >= n-1:
            hike = True
        if slope and inc >= m-1:
            valley += 1
            slope = False
    elif a[i+1] < a[i]:
        inc = 0
        slope = False
        dec += 1
        if dec >= m-1:
            slope = True
        if hike and dec >= n-1:
            peak += 1
            hike = False
print(peak, valley)
