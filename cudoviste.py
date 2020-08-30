r, c = map(int, input().split())
lot = []
for _ in range(r):
    lot.append(list(input()))
smashed = [0, 0, 0, 0, 0]
for j in range(r-1):
    for i in range(c-1):
        cells = [lot[j][i], lot[j+1][i], lot[j][i+1], lot[j+1][i+1]]
        if cells.count('#') == 0:
            smashed[cells.count('X')] += 1
for x in smashed:
    print(x)
