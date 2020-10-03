a = [2, 3, 5, 7, 11, 13, 17, 19]
x = [1]
for n in a[:-1]:
    x.append(x[-1]*n)

l = list(map(int, input().split()))
ans = 0
for i in range(8):
    ans += (a[i] - l[i] - 1) * x[i]
print(ans)
