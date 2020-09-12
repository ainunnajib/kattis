s = input().split()
h = int(s[0])
if len(s) > 1:
    s = s[1]
    l = len(s)
    n = 1 << (h+1)
    for i in range (l+1):
        n -= (1 << i)
    for i in range(l):
        n += ((1 << i) if s[l-i-1] == 'L' else 0)
    print(n)
else:
    print((1 << (h+1)) - 1)
