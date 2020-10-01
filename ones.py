from sys import stdin

for n in stdin.readlines():
    n = int(n)

    x = 1
    ans = 1
    while x % n != 0:
        x = x * 10 + 1
        x %= n
        ans += 1

    print(ans)
