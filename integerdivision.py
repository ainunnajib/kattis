from collections import defaultdict
n, d = map(int, input().split())

l = list(map(int, input().split()))
groups = defaultdict(int)
for x in l:
    groups[x//d] += 1

ans = 0
for k in groups:
    ans += groups[k] * (groups[k] - 1) // 2

print(ans)
