a = 'abcdefghijklmnopqrstuvwxyz'
n, m = map(int, input().split())
k = [a.index(x) for x in input()]
k = k[::-1]
s = [a.index(x) for x in input()]
s = s[::-1]
for i in range(m):
    k.append((s[i]-k[i])%26)
k = k[::-1][n:]
r = [a[x] for x in k]
print(''.join(r))
