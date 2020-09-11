from collections import defaultdict
t = int(input())
for _ in range(t):
    d = defaultdict(int)
    n = int(input())
    for __ in range(n):
        s = input().split()
        d[s[0]] += int(s[1])

    srt = defaultdict(list)
    for x in set(sorted(d.values(), reverse = True)):
        for k in d:
            if x == d[k]:
                srt[x].append(k)
    
    print(len(d))
    for x in srt:
        for y in sorted(srt[x]):
            print(y, x)
