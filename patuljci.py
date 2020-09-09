from itertools import combinations
n = []
for _ in range(9):
    n.append(int(input()))
for c in combinations(n, 7):
    if sum(c) == 100:
        for x in c:
            print(x)
        break
