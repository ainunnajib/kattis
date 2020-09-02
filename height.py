p = int(input())
for _ in range(p):
    s = list(map(int, input().split()))
    k = s[0]
    a = s[1:]
    s = [a[0]]
    steps = 0
    for i in range(1, len(a)):
        inserted = False
        for j in range(len(s)):
            if s[j] > a[i]:
                steps += len(s) - j
                s = s[:j] + a[i:i+1] + s[j:]
                inserted = True
                break
        if not inserted:
            s = s + a[i:i+1]
    print(k, steps)
