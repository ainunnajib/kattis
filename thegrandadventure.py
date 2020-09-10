n = int(input())
for _ in range(n):
    s = input()
    b = []
    success = True
    for c in s:
        if c in '$|*':
            if c == '$':
                b.append('b')
            elif c == '|':
                b.append('t')
            else:
                b.append('j')
        elif c in 'tjb':
            if len(b) > 0:
                x = b.pop(-1)
                while x != c and len(b) > 0:
                    x = b.pop(-1)
                if len(b) == 0 and x != c:
                    success = False
                    break
            else:
                success = False
                break
    if success and len(b) == 0:
        print('YES')
    else:
        print('NO')
