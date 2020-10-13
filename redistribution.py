n = int(input())
s = list(map(int, input().split()))
l = []
for i in range(n):
    l.append((s[i], i+1))
l.sort(reverse = True)
s.sort(reverse = True)

if s[0] > sum(s[1:]):
    print('impossible')
else:
    ans = []
    for t in l:
        ans.append(str(t[1]))
    print(' '.join(ans))
