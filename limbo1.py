t = int(input())
for _ in range(t):
    l, r = map(int, input().split())
    n = l+r+1
    x = (n*(n+1))//2
    x -= l
    print(x)
