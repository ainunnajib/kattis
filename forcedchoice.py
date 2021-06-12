n, p, s = map(int, input().split())
for _ in range(s):
    l = list(map(int, input().split()))
    m = l[0]
    l = l[1:]
    if p in l:
        print('KEEP')
    else:
        print('REMOVE')