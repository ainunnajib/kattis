from collections import defaultdict
t = int(input())
for _ in range(t):
    tonative = defaultdict(set)
    toforeign = defaultdict(set)
    n = int(input())
    for __ in range(n):
        p = input()
        s = input().split()
        x = s[1:]
        s = input().split()
        y = s[1:]

        for i in x:
            if len(tonative[i]) == 0:
                tonative[i] = set(y)
            else:
                tonative[i] = tonative[i].intersection(set(y))

        for i in y:
            if len(toforeign[i]) == 0:
                toforeign[i] = set(x)
            else:
                toforeign[i] = toforeign[i].intersection(set(x))

    for x in sorted(tonative.keys()):
        for y in sorted(tonative[x]):
            if x in toforeign[y]:
                print('(' + x + ', ' + y + ')')

    if _ < t-1:
        print()
