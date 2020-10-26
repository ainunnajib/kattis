n, m, k = map(int, input().split())
lp = list(map(int, input().split()))
lc = list(map(int, input().split()))
ls = list(map(int, input().split()))

lp = [2*(x**2) for x in lp]
lc = [2*(x**2) for x in lc]
ls = [x**2 for x in ls]
lh = lc + ls

lp.sort()
lh.sort()

i = 0
count = 0
done = False
for h in lh:
    while h >= lp[i]:
        i += 1
        if i == n:
            done = True
            break
    if done:
        break
    count += 1
    i += 1
    if i == n:
        break

print(count)
