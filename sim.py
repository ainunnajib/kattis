from sys import *
for _ in range(int(input())):
    s = input()
    # typing char always append/insert ahead except at home
    athome = True
    prv, nxt = {}, {}
    start, cur, end = -1, -1, -1

    for i in range(len(s)):
        c = s[i]
        x, y, z = -1, cur, -1
        if cur >= 0:
            x = prv[cur]
            z = nxt[cur]

        if c == '\n':
            break
        elif c == '[':
            athome = True
            cur = start
        elif c == ']':
            athome = False
            cur = end
        elif c == '<':
            if not athome:
                if x >= 0:
                    nxt[x] = z
                    cur = x
                else:
                    athome = True
                    start, cur = z, z
                if z >= 0:
                    prv[z] = x
                if end == y:
                    end = x
        else:
            cur = i
            if athome:
                prv[cur] = -1
                nxt[cur] = start
                prv[start] = cur
                start = cur
                athome = False
            else:
                nxt[y] = cur
                prv[cur] = y
                nxt[cur] = z
            
                if end == y:
                    end = cur

            if end < 0:
                end = cur

    if start >= 0:
        stdout.write(s[start])
        while nxt[start] >= 0:
            start = nxt[start]
            stdout.write(s[start])
    stdout.write('\n')
stdout.flush()