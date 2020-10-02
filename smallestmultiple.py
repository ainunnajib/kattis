from sys import stdin
for line in stdin.readlines():
    l = list(map(int, line.split()))
    ans = l[0]
    for n in l[1:]:
        x, y = ans, n
        while y > 0:
            x, y = y, x%y
        ans *= n // x

    print(ans)
