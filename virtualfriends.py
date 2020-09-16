from collections import defaultdict
t = int(input())
for _ in range(t):
    size = defaultdict(int)
    idx = {}
    setdict = defaultdict(set)
    n = int(input())
    for __ in range(n):
        a, b = input().split()
        if a in idx and b in idx:
            if idx[a] == idx[b]:
                s = len(setdict[idx[a]])
            else:
                ia = idx[a]
                ib = idx[b]
                seta = setdict[ia]
                setb = setdict[ib]
                setu = seta.union(setb)
                s = len(setu)
                for x in idx:
                    if idx[x] in (ia, ib):
                        idx[x] = ia
                        setdict[x] = setu
        elif a in idx:
            setdict[idx[a]].add(b)
            idx[b] = idx[a]
            s = len(setdict[idx[a]])
        elif b in idx:
            setdict[idx[b]].add(a)
            idx[a] = idx[b]
            s = len(setdict[idx[b]])
        else:
            setu = set()
            setu.add(a)
            setu.add(b)
            setdict[a] = setu
            idx[a] = a
            idx[b] = a
            s = 2
        print(s)
