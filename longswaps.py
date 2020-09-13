s = input().split()
k = int(s[1])
s = s[0]
n = len(s)
if k <= n//2:
    print('Yes')
else:
    x = s[n-k:k]
    s = ''.join(sorted(s))
    if x == s[n-k:k]:
        print('Yes')
    else:
        print('No')
