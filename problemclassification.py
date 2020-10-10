from collections import defaultdict

cat = defaultdict(set)
n = int(input())
for _ in range(n):
    s = input().split()
    for x in s[2:]:
        cat[x].add(s[0])

d = defaultdict(int)
while True:
    try:
        for w in input().split():
            if w in cat:
                for c in cat[w]:
                    d[c] += 1
    except EOFError:
        if len(d) == 0:
            ans = []
            for s in cat.values():
                for k in s:
                    ans.append(k)
        else:
            maxmatch = max(d.values())
            ans = []
            for k in d:
                if d[k] >= maxmatch:
                    ans.append(k)

        ans.sort()
        for a in ans:
            print(a)
        break
