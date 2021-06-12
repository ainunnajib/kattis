from collections import defaultdict
t = int(input())
for _ in range(t):
    df = defaultdict(set)
    dn = defaultdict(set)
    n = int(input())
    for __ in range(n):
        pizza = input()
        foreigns = input().split()[1:]
        for f in foreigns:
            df[f].add(pizza)
        natives = input().split()[1:]
        for n in natives:
            dn[n].add(pizza)

    for f in sorted(df.keys()):
        for n in sorted(dn.keys()):
            if df[f] == dn[n]:
                print('(' + f + ', ' + n + ')')

    if _ < t-1:
        print()
