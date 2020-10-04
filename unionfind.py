n, q = map(int, input().split())
ufds = {i:i for i in range(n)}
for _ in range(q):
    s = input().split()
    a, b = map(int, s[1:])

    update = set()
    x = ufds[a]
    update.add(a)
    while x != ufds[x]:
        update.add(x)
        x = ufds[x]
    for node in update:
        ufds[node] = x

    update = set()
    y = ufds[b]
    update.add(b)
    while y != ufds[y]:
        update.add(y)
        y = ufds[y]
    for node in update:
        ufds[node] = y

    if s[0] == '?':
        print('yes' if x == y else 'no')
    elif s[0] == '=':
        ufds[y] = x
