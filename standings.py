t = int(input())
for _ in range(t):
    input()
    n = int(input())
    l = []
    for __ in range(n):
        s = input().split()
        l.append(int(s[1]))
    l.sort()
    bad = 0
    for i in range(n):
        bad += abs(i+1-l[i])
    print(bad)
