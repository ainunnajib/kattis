class UFDS:
    def __init__(self, n):
        self.parents = list(range(n))
        self.ranks = [0] * n
        self.sizes = [1] * n
        self.balances = [0] * n
        self.numdisjoint = n

    def find(self, x):
        xp = x
        children = []
        while xp != self.parents[xp]:
            children.append(xp)
            xp = self.parents[xp]
        for c in children:
            self.parents[c] = xp
        return xp

    def union(self, a, b):
        ap = self.find(a)
        bp = self.find(b)
        if ap == bp:
            return

        if self.ranks[ap] < self.ranks[bp]:
            self.parents[ap] = bp
            self.sizes[bp] += self.sizes[ap]
            self.balances[bp] += self.balances[ap]
        elif self.ranks[bp] < self.ranks[ap]:
            self.parents[bp] = ap
            self.sizes[ap] += self.sizes[bp]
            self.balances[ap] += self.balances[bp]
        else:
            self.parents[bp] = ap
            self.ranks[ap] += 1
            self.sizes[ap] += self.sizes[bp]
            self.balances[ap] += self.balances[bp]

        self.numdisjoint -= 1

    def size(self, x):
        return self.sizes[self.find(x)]

n, m = map(int, input().split())
u = UFDS(n)

for i in range(n):
    u.balances[i] = int(input())

for _ in range(m):
    a, b = map(int, input().split())
    u.union(a, b)

possible = True
for i in range(n):
    if u.balances[u.find(i)] != 0:
        possible = False
        break

print('POSSIBLE' if possible else 'IMPOSSIBLE')
