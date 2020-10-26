from sys import stdin, stdout
n, m = map(int, stdin.readline().split())
w = list(map(int, stdin.readline().split()))
w.sort(reverse = True)

l = []
for _ in range(m):
    x, p = map(int, stdin.readline().split())
    l.append((p, x))
l.sort(reverse = True)

money = 0
i = 0
j = 0
while n > 0:
    sold = min(l[j][1], n)
    money += sum(w[i:i+sold]) * l[j][0]
    n -= sold
    i += sold
    j += 1
    if j == m:
        break

stdout.write(str(money))
