n = int(input())
while n != 0:
    d = {}
    for _ in range(n):
        s = input().split()
        for x in s[1:]:
            if x not in d:
                d[x] = [s[0]]
            else:
                d[x].append(s[0])
    for x in d:
        d[x].sort()
    l = list(d.keys())
    l.sort()
    for x in l:
        print(x, ' '.join(d[x]))
    print()
    
    n = int(input())
