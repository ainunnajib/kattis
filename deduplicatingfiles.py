from collections import defaultdict

n = int(input())
while n > 0:
    files = defaultdict(int)
    hashes = defaultdict(dict)

    for _ in range(n):
        f = input()
        files[f] += 1
        b = int.from_bytes(f[0].encode(), "big")
        for c in f[1:]:
            x = int.from_bytes(c.encode(), "big")
            b = b^x
        if b not in hashes:
            hashes[b] = defaultdict(int)
        hashes[b][f] += 1

    collisions = 0
    for k in hashes:
        for f1 in hashes[k]:
            for f2 in hashes[k]:
                if f1 != f2:
                    collisions += hashes[k][f1] * hashes[k][f2]

    print(len(files), collisions//2)
    n = int(input())
