import math
n = int(input())
rank = []
for i in range(n):
    s, p, f, o = map(int, input().split())
    s = -1 * s
    o = -1 * o
    rank.append((s, p, f, o, i))
rank.sort()
score = [100, 75, 60, 50, 45, 40, 36, 32, 29, 26, 24, 22, 20, 18, 16,
         15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
finalscore = []
buffer = []
bufferscore = 0
prev = (1, -1, -1)
for i in range(n):
    t = rank[i]
    cur = (t[0], t[1], t[2])
    if cur == prev or buffer == []:
        buffer.append(t)
        if i < 30:
            bufferscore += score[i]
    else:
        sc = math.ceil(bufferscore/len(buffer))
        for b in buffer:
            finalscore.append((b[4], sc-b[3]))
        buffer = []
        if i < 30:
            bufferscore = score[i]
        else:
            bufferscore = 0
        buffer.append(t)
    prev = cur
if len(buffer) > 0:
    sc = math.ceil(bufferscore/len(buffer))
    for b in buffer:
        finalscore.append((b[4], sc-b[3]))

finalscore.sort()
for f in finalscore:
    print(f[1])
