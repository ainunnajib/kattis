n = int(input())
d = list(map(int, input().split()))
dirty = 0
dirtiness = 0
cleanup = 0
i = d[0]
for j in range(n):
    while i < d[j]: # while today hasn't reach the next dirty push
        if dirtiness + dirty >= 20: # tomorrow hits 20, cleanup today
            cleanup += 1
            dirtiness = 0
            dirty = 0
        dirtiness += dirty
        i += 1 # move to tomorrow
    dirty += 1 # count today's dirty push for next processing
    if dirtiness + dirty >= 20: # tomorrow hits 20, cleanup today
        cleanup += 1
        dirtiness = 0
        dirty = 0
if dirty > 0:
    print(cleanup+1)
else:
    print(cleanup)
