n, m = map(int, input().split())
l = []
for i in range(1, n+1):
    s = input().split()
    f = int(s[0])
    s = s[1]
    l.append((f*i, n-i, s))
l.sort(reverse = True)
for i in range(m):
    print(l[i][2])
