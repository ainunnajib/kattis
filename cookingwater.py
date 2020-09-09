n = int(input())
start = -1
end = 1001
for _ in range(n):
    s, e = map(int, input().split())
    start = max(start, s)
    end = min(end, e)
if start <= end:
    print('gunilla has a point')
else:
    print('edward is right')
