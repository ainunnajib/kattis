t = int(input())
for _ in range(t):
    x = input()
    maxi = 0
    for j in range(1, len(x)+1):
        i = 0
        c = int(x[:j])
        while c > 0:
            i += c%2
            c //= 2
        maxi = max(maxi, i)
    print(maxi)
