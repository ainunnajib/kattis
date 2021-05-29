n, k = map(int, input().split())
t = 0
for _ in range(k):
    t += int(input())
print((t - (n-k)*3) / n, (t + (n-k)*3) / n)
