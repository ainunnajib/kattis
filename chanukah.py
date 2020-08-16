p = int(input())
for _ in range(p):
    k, n = map(int, input().split())
    print(k, int(n*(n+3)/2))
