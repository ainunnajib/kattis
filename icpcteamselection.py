t = int(input())
for _ in range(t):
    n = int(input())
    s = list(map(int, input().split()))
    s.sort(reverse = True)
    print(sum(s[1:2*n:2]))
