c = int(input())
for _ in range(c):
    n, m = map(int, input().split())
    totalprize = 0
    stickers, prizes, count = [], [], []
    for __ in range(n):
        s = list(map(int, input().split()))
        stickers.append(s[1:-1])
        count.append([0]*len(s[1:-1]))
        prizes.append(s[-1])
    s = list(map(int, input().split()))
    for j in range(len(s)):
        for i in range(n):
            if j+1 in stickers[i]:
                count[i][stickers[i].index(j+1)] += s[j]
    for i in range(n):
        totalprize += min(count[i])*prizes[i]
    print(int(totalprize))
