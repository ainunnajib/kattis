n, m = map(int, input().split())
p = list(map(int, input().split()))
t = list(map(int, input().split()))
p.sort()
t.sort()
taken = [False for _ in range(m)]
for x in p:
    mindist = 10000
    tx = -1
    while tx < m-1 and abs(t[tx+1] - x) < mindist:
        tx += 1
        mindist = abs(t[tx] - x)
    taken[tx] = True
print(n - sum(taken))