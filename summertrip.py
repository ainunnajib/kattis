s = input()
ls = len(s)

ans = 0
for i in range(ls-1):
    d = set()
    for j in range(i+1, ls):
        if s[i] == s[j]:
            break
        if s[j] not in d:
            ans += 1
        d.add(s[j])
print(ans)
