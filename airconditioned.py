n = int(input())
l = []
for _ in range(n):
    a, b = map(int, input().split())
    l.append((a, b))
l.sort()

count = 0
mintemp = 0
maxtemp = 0
for t in l:
    if t[0] > maxtemp or t[1] < mintemp:
        count += 1
        mintemp = t[0]
        maxtemp = t[1]
    else:
        mintemp = max(mintemp, t[0])
        maxtemp = min(maxtemp, t[1])

print(count)
