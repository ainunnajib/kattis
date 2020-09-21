t = int(input())
for _ in range(t):
    p = input()
    n = int(input())
    s = input()
    if s == '[]':
        l = []
    else:
        l = list(map(int, s[1:-1].split(',')))

    error = False
    reverse = False
    i = 0
    j = n-1
    for c in p:
        if c == 'R':
            reverse = not reverse
        elif c == 'D':
            if i > j:
                error = True
                break
            elif reverse:
                j -= 1
            else:
                i += 1
    if error:
        print('error')
    else:
        if reverse:
            s = [str(l[x]) for x in range(j,i-1,-1)]
        else:
            s = [str(x) for x in l[i:j+1]]
        print('[' + ','.join(s) + ']')
