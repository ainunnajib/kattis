n, m = map(int, input().split())
t = list(map(int, input().split()))
l = list(map(int, input().split()))
t.sort()
l.sort()


i = 0
count = 0
done = False
for task in t:
    while l[i] < task:
        i += 1
        if i == m:
            done = True
            break
    if done:
        break
    count += 1
    i += 1
    if i == m:
        done = True
        break

print(count)
