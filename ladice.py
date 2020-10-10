class UFDS:
    def __init__(self, n):
        self.parents = list(range(n))
        self.ranks = [0] * n
        self.sizes = [1] * n
        self.taken = [0] * n
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
            self.taken[bp] += self.taken[ap]
        elif self.ranks[bp] < self.ranks[ap]:
            self.parents[bp] = ap
            self.sizes[ap] += self.sizes[bp]
            self.taken[ap] += self.taken[bp]
        else:
            self.parents[bp] = ap
            self.ranks[ap] += 1
            self.sizes[ap] += self.sizes[bp]
            self.taken[ap] += self.taken[bp]

        self.numdisjoint -= 1

    def size(self, x):
        return self.sizes[self.find(x)]

    def issameset(self, a, b):
        return self.find(a) == self.find(b)

    def takeslot(self, a):
        ap = self.find(a)

        if self.taken[ap] < self.sizes[ap]:
            self.taken[ap] += 1
            return True
        else:
            return False

n, l = map(int, input().split())
u = UFDS(l)
for _ in range(n):
    a, b = map(int, input().split())
    a -= 1
    b -= 1

    u.union(a, b)
    print('LADICA' if u.takeslot(a) else 'SMECE')
