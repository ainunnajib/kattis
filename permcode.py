x = int(input())
while x != 0:
    s = input()
    p = input()
    c = input()
    n = len(c)
    m = [''] * n
    ms = [0] * n
    mp = [0] * n
    d = int(n**1.5 + x) % n

    # pivot first i.e. c[d] = s[mp[d]]
    mp[d] = s.index(c[d])
    m[d] = p[mp[d]]
    ms[d] = s.index(m[d])

    # rule: c[i] = s[mp[i] ^ ms[(i+1)%n]]
    i = (d-1)%n
    while i != d:
        mp[i] = s.index(c[i]) ^ ms[(i+1)%n]
        m[i] = p[mp[i]]
        ms[i] = s.index(m[i])
        i = (i-1)%n

    print(''.join(m))

    x = int(input())
