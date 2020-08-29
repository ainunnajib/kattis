n, p = map(int, input().split())
t = list(map(int, input().split()))
k = list(map(int, input().split()))
print(max(t)*(p-1)+sum(t))
