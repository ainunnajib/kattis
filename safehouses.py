n = int(input())
spies = []
safehouses = []
for r in range(n):
    s = input()
    for c in range(n):
        if s[c] == 'S':
            spies.append((r, c))
        if s[c] == 'H':
            safehouses.append((r, c))

maxdist = 0
for s in spies:
    mindist = 2 * n
    for h in safehouses:
        mindist = min(mindist, abs(h[0]-s[0]) + abs(h[1]-s[1]))

    maxdist = max(maxdist, mindist)

print(maxdist)
