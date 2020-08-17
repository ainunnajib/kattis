n, b, h, w = map(int, input().split())
cost = 1000000
for _ in range(h):
    p = int(input())
    a = list(map(int, input().split()))
    if max(a) >= n:
        cost = min(cost, p*n)
if cost > b:
    print("stay home")
else:
    print(cost)
