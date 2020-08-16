n, r, k = map(int, input().split())
steps = k + abs(k-r)
if steps < n:
    if (n-steps)%2 == 0:
        print(n+r)
    else:
        print(n+r+1)
else:
    print(steps+r)
