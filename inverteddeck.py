n = int(input())
a = list(map(int, input().split()))
s = sorted(a)
if a == s:
    print(1, 1)
else:
    start = 0
    for i in range(n):
        if a[i] != s[i]:
            start = i
            break
    end = n-1
    for i in range(n-1,-1,-1):
        if a[i] != s[i]:
            end = i
            break
    if (a[:start] + a[start:end+1][::-1] + a[end+1:]) == s:
        print(start+1, end+1)
    else:
        print('impossible')
