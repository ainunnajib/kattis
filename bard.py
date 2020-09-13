n = int(input())
d = [{} for _ in range(n)]
e = int(input())
for song in range(e):
    s = list(map(int, input().split()))
    s = [x-1 for x in s[1:]]
    if min(s) == 0:
        for x in s:
            d[x][song] = True
    else:
        all = {}
        for x in s:
            for song in d[x]:
                all[song] = True
        for x in s:
            for song in all:
                d[x][song] = True
maxsong = max([len(d[x]) for x in range(n)])
for x in range(n):
    if len(d[x]) == maxsong:
        print(x+1)
