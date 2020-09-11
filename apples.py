from collections import defaultdict
r, c = map(int, input().split())
apples = defaultdict(int)
empty = defaultdict(int)
columns = [[] for i in range(c)]

for _ in range(r):
    s = list(input())
    for i in range(c):
        if s[i] == 'a':
            apples[i] += 1
        elif s[i] == '.':
            empty[i] += 1
        elif s[i] == '#':
            columns[i].extend(['.' for _ in range(empty[i])])
            columns[i].extend(['a' for _ in range(apples[i])])
            empty[i] = 0
            apples[i] = 0
            columns[i].append('#')
for i in range(c):
    columns[i].extend(['.' for _ in range(empty[i])])
    columns[i].extend(['a' for _ in range(apples[i])])
    empty[i] = 0
    apples[i] = 0

for j in range(r):
    print(''.join([columns[i][j] for i in range(c)]))
