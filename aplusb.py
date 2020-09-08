from itertools import combinations
n = int(input())
a = list(map(int, input().split()))
a.sort()
count = 0
for t in combinations(range(n), 3):
    if a[t[0]] + a[t[1]] == a[t[2]]:
        count += 1
    if a[t[1]] + a[t[2]] == a[t[0]]:
        count += 1
    if a[t[0]] + a[t[2]] == a[t[1]]:
        count += 1
print(count*2)
