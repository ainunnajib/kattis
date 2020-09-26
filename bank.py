n, k = map(int, input().split())
l = [0 for i in range(k)]
q = []
for _ in range(n):
    c, t = map(int, input().split())
    q.append((c, t))
q.sort(reverse = True)
done = 0
for x in q:
    i = x[1]
    while l[i] != 0 and i >= 0:
        i -= 1
    if i >= 0:
        l[i] = x[0]
        done += 1
    if done == k:
        break
print(sum(l))
