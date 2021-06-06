n = int(input())
ct, cd = map(int, input().split())
maxspeed = 0
for _ in range(n-1):
    t, d = map(int, input().split())
    maxspeed = max(maxspeed, (d-cd)//(t-ct))
    ct, cd = t, d
print(maxspeed)