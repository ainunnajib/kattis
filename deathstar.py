n = int(input())
l = []
for i in range(n):
    s = list(map(int, input().split()))
    x = 0
    for b in s:
        x = x | b
    l.append(x)

s = [str(x) for x in l]
print(' '.join(s))
