l, h = map(int, input().split())
ans = 0
for x in range(l, h+1):
    d = sorted(list(map(int, list(str(x)))))
    if 0 in d:
        continue
    unique = True
    alldiv = True
    for i in range(len(d)-1):
        if d[i] == d[i+1]:
            unique = False
        if x%d[i] != 0:
            alldiv = False
    if x%d[len(d)-1] != 0:
        alldiv = False
    if unique and alldiv:
        ans += 1
print(ans)
