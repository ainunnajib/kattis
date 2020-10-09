import sys

d = '0125986'

for line in sys.stdin.readlines():
    k = int(line)
    ans = ''
    while k > 0:
        ans += d[k%7]
        k //= 7
    print(ans)
