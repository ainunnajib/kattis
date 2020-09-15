n = int(input())
a, b = [], []
for i in range(n):
    x, y = map(int, input().split())
    a.append(x)
    b.append(y)
    x = sorted(a)
    y = sorted(b, reverse = True)
    maxsum = 0
    for j in range(i+1):
        maxsum = max(maxsum, x[j] + y[j])
    print(maxsum)
