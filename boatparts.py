p, n = map(int, input().split())
d = {}
for i in range(n):
    d[input()] = True
    if len(d) == p:
        print(i+1)
        break
if len(d) < p:
    print('paradox avoided')
