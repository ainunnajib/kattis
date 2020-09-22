s, c, k = map(int, input().split())
d = list(map(int, input().split()))
d.sort()
num = 1
cur = 0
minsock = d[0]
for sock in d:
    if sock - minsock > k or cur == c:
        num += 1
        cur = 1
        minsock = sock
    else:
        cur += 1
print(num)
