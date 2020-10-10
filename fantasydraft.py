from collections import defaultdict

n, k = map(int, input().split())

pref = [[] for _ in range(n)]
for i in range(n):
    s = input().split()
    if s[0] != '0':
        pref[i].extend(s[1:])

p = int(input())
playerslist = []
available = set()
for _ in range(p):
    player = input()
    playerslist.append(player)
    available.add(player)

selected = [[] for _ in range(n)]
cur = 0
for t in range(k):
    for o in range(n):
        s = ''
        for pr in pref[o]:
            if pr in available:
                s = pr
                available.remove(pr)
                break
        if s == '':
            while playerslist[cur] not in available:
                cur += 1
            s = playerslist[cur]
            available.remove(s)

        selected[o].append(s)

for o in range(n):
    print(' '.join(selected[o]))
