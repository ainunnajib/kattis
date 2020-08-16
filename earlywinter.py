n, m = map(int, input().split())
d = list(map(int, input().split()))
x = 0
for i in range(n):
    if d[i] <= m:
        break
    x += 1
if x == n:
    print("It had never snowed this early!")
else:
    print("It hadn't snowed this early in " + str(x) + " years!")
