r, c, f, s, g = map(int, input().split())

fcoor = [[] for _ in range(f)]
for j in range(f):
    sf = list(map(int, input().split()))
    for i in range(sf[0]):
        y, x = sf[1+i*2] - 1, sf[2+i*2] - 1
        fcoor[j].append((y, x))
    fcoor[j].sort()

scoor = {}
sfac = {}
facs = [[] for _ in range(f)]
for _ in range(s):
    y, x, id, fac = map(int, input().split())
    scoor[id] = (y-1, x-1)
    sfac[id] = fac-1
    facs[fac-1].append(id)

tmin = list(map(int, input().split()))

fdist = [[] for _ in range(f)]
for i in range(f):
    j = 0
    for student in sorted(facs[i]):
        starty, startx = scoor[student]
        endy, endx = fcoor[i][j]
        j += 1

        dist = abs(startx-endx) + abs(starty-endy)
        fdist[i].append(dist)
    fdist[i].sort()

facdist = [0 for _ in range(f)]
for i in range(f):
    minstudents = tmin[i]
    facdist[i] = sum(fdist[i][:minstudents])
facdist.sort()

print(sum(facdist[:g]))
