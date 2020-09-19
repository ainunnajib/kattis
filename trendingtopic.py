from collections import defaultdict
l = []
while True:
    try:
        s = input()
        if s == '<text>':
            l.append(defaultdict(int))
            s = input()
            while s != '</text>':
                for w in s.split():
                    if len(w) > 3:
                        l[-1][w] += 1
                s = input()
        elif s[:4] == '<top':
            s = s.split()
            n = int(s[1])
            dd = defaultdict(int)
            for d in l[-7:]:
                for w in d:
                    dd[w] += d[w]
            ll = []
            for k in dd:
                ll.append((-1*dd[k], k))
            ll.sort()
            rank = []
            for f in ll:
                rank.append(f[0])
                if len(rank) == n:
                    break

            print('<top', str(n) + '>')
            for x in ll:
                if x[0] in rank:
                    print(x[1], -1*x[0])
            print('</top>')
    except EOFError:
        break
