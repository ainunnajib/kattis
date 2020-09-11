r, c = map(int, input().split())
columns = [[] for _ in range(c)]
buffer = [[] for _ in range(c)]
for _ in range(r):
    s = list(input())
    for i in range(c):
        if s[i] == 'a':
            buffer[i].append('a')
        elif s[i] == '.':
            buffer[i].insert(0, '.')
        elif s[i] == '#':
            columns[i].extend(buffer[i])
            buffer[i] = []
            columns[i].append('#')
for i in range(c):
    columns[i].extend(buffer[i])

for j in range(r):
    print(''.join([columns[i][j] for i in range(c)]))
