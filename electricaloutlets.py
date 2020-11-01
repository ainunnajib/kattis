n = int(input())
for _ in range(n):
    l = list(map(int, input().split()))
    k = l[0]
    l = l[1:]
    print(sum(l)+1-k)
