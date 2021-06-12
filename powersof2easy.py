n, e = map(int, input().split())
x = str(2**e)
ans = 0
for i in range(n+1):
    if x in str(i):
        ans += 1
print(ans)