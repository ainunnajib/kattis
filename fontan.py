n, m = map(int, input().split())
l = []
for _ in range(n):
    l.append(list(input()))

changed = True
while changed:
    changed = False
    for i in range(n):
        for j in range(m):
            if l[i][j] == 'V':
                if i == n-1:
                    continue
                if l[i+1][j] == 'V':
                    continue
                if l[i+1][j] == '.':
                    l[i+1][j] = 'V'
                    changed = True
                elif l[i+1][j] == '#':
                    if j > 0:
                        if l[i][j-1] == '.':
                            l[i][j-1] = 'V'
                            changed = True
                    if j < m-1:
                        if l[i][j+1] == '.':
                            l[i][j+1] = 'V'
                            changed = True

for r in l:
    print(''.join(r))
