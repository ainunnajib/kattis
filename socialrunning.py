n = int(input())
d = []
for _ in range(n):
    d.append(int(input()))
mindist = 2*max(d)
for i in range(n):
    mindist = min(mindist, d[i] + d[(i-2)%n])
print(mindist)
