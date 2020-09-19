n, k = map(int, input().split())
s = input().split()
l = [0]
undo = False
for c in s:
    if undo:
        # do undo
        x = int(c)
        for _ in range(x):
            l.pop()
        undo = False
    elif c == 'undo':
        undo = True
    else:
        x = int(c)
        l.append((l[-1]+x)%n)
print(l[-1])
