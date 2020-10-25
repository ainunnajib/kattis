n = int(input())
l = list(map(int, input().split()))

d = {}
i = 0
ans = []
for c in l:
    while c not in d:
        x = (i^(i << 1)) % 256
        d[x] = i
        i += 1
    ans.append(str(d[c]))
print(' '.join(ans))
