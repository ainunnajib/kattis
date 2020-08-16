n = int(input())
t = list(map(int, input().split()))
start = 0
mint = max(t[0], t[2])
for i in range(n-2):
    if mint > max(t[i], t[i+2]):
        start = i
        mint = max(t[i], t[i+2])
print(start+1, mint)
