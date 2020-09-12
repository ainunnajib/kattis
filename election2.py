n = int(input())
d = {}
v = {}
for _ in range(n):
    a = input()
    p = input()
    d[a] = p
    v[a] = 0

m = int(input())
for _ in range(m):
    a = input()
    if a in v:
        v[a] += 1
win = max(v.values())
winner = [k for k in v if v[k] == win]
if len(winner) > 1:
    print('tie')
else:
    print(d[winner[0]])
