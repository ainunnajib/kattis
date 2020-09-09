from collections import defaultdict
n = int(input())
rlist, flist, olist = [], [], []
first = defaultdict(list)
other = defaultdict(list)
for _ in range(n):
    r, f, o = input().split()
    f = float(f)
    o = float(o)
    first[f].append(r)
    other[o].append(r)
    rlist.append(r)
    flist.append(f)
    olist.append(o)

min4o = sorted(olist)[:4]
team = []
for t in min4o:
    i = olist.index(t)
    while i in team:
        i = olist[i+1:].index(t) + i + 1
    team.append(i)
min = 100
finalteam = []
for i in range(n):
    if i in team:
        t = flist[i] + sum(min4o) - min4o[team.index(i)]
        if min > t:
            min = t
            finalteam = [i]
            for x in team:
                if x != i:
                    finalteam.append(x)
    else:
        t = flist[i] + sum(min4o[:3])
        if min > t:
            min = t
            finalteam = [i] + team[:3]

print(min)
for x in finalteam:
    print(rlist[x])
