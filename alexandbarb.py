k, m, n = map(int, input().split())
if k%(m+n) < m:
    print('Barb')
else:
    print('Alex')
