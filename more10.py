class UFDS:
    def __init__(self, n):
        self.parents = list(range(n))
        self.ranks = [0] * n
        self.sizes = [1] * n
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
        elif self.ranks[bp] < self.ranks[ap]:
            self.parents[bp] = ap
            self.sizes[ap] += self.sizes[bp]
        else:
            self.parents[bp] = ap
            self.ranks[ap] += 1
            self.sizes[ap] += self.sizes[bp]

        self.numdisjoint -= 1

    def size(self, x):
        return self.sizes[self.find(x)]

words = set()
iss = []
nots = []
n = int(input())
for _ in range(n):
    s = input().split()

    words.add(s[0])
    words.add(s[0][-3:])
    words.add(s[2])
    words.add(s[2][-3:])

    if s[1] == 'is':
        iss.append((s[0], s[2]))
    else:
        nots.append((s[0], s[2]))

i = 0
d = {}
for w in words:
    d[w] = i
    i += 1

u = UFDS(i)

for w in words:
    u.union(d[w], d[w[-3:]])
    if w[-2:] in words:
        u.union(d[w], d[w[-2:]])
    if w[-1] in words:
        u.union(d[w], d[w[-1]])

for t in iss:
    a, b = t
    u.union(d[a], d[b])

consistent = True
for t in nots:
    a, b = t
    if u.find(d[a]) == u.find(d[b]):
        consistent = False
        break
print('yes' if consistent else 'wait what?')
