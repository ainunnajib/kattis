n, k = map(int, input().split())
a, s = map(int, input().split())
x = (n*a - k*s)/(n-k)
if x < 0 or x > 100:
    print('impossible')
else:
    print(x)