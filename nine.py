modulo = 1000000007
l = [9]
x = 9
for _ in range(60):
    x = (x*x)%modulo
    l.append(x)

t = int(input())
for _ in range(t):
    n = int(input())
    n -= 1
    ans = 8
    for x in l:
        if n%2 == 1:
            ans = (ans*x)%modulo
        n //= 2
        if n == 0:
            break
    print(ans)
