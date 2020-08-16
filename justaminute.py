n = int(input())
totalm = 0
totals = 0
for i in range(n):
    l = input().split()
    totalm += int(l[0])
    totals += int(l[1])
ans = 1.0*totals/totalm/60
if ans <= 1:
    print("measurement error")
else:
    print(ans)
