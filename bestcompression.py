n, b = map(int, input().split())
for _ in range(b+1):
    n //= 2
if n == 0:
    print('yes')
else:
    print('no')
