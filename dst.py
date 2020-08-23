n = int(input())
for _ in range(n):
    s = input().split()
    c = -1 if s[0] == 'B' else 1
    d = int(s[1])
    h = int(s[2])
    m = int(s[3])
    t = h*60 + m
    t += c*d
    t %= (24*60)
    h = t // 60
    m = t % 60
    print(h, m)
