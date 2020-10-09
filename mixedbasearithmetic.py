import sys

l = 'abcdefghijklmnopqrstuvwxyz'
u = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
d = '0123456789'

for line in sys.stdin.readlines():
    s = line.split()
    a = list(s[0][::-1])
    i = int(s[1])

    ans = []
    for c in a:
        if c in d:
            x = int(c) + i%10
            ans.append(str(x%10))
            i = i//10 + x//10
        elif c in l:
            x = l.index(c) + i%26
            ans.append(l[x%26])
            i = i//26 + x//26
        elif c in u:
            x = u.index(c) + i%26
            ans.append(u[x%26])
            i = i//26 + x//26

    while i > 0:
        c = a[-1]
        if c in d:
            ans.append(str(i%10))
            i = i//10
        elif c in l:
            i -= 1
            ans.append(l[i%26])
            i = i//26
        elif c in u:
            i -= 1
            ans.append(u[i%26])
            i = i//26

    print(''.join(ans)[::-1])
