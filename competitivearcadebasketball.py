n, p, m = map(int, input().split())
d = {}
w = {}
for _ in range(n):
    d[input()] = 0
for _ in range(m):
    a, k = input().split()
    k = int(k)
    d[a] += k
    if d[a] >= p and a not in w:
        print(a, 'wins!')
        w[a] = True
if len(w) == 0:
    print('No winner!')
