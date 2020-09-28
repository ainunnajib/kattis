s = input()
ls = len(s)
ans = s
for i in range(1, ls-1):
    for j in range(i+1, ls):
        a = s[:i][::-1] + s[i:j][::-1] + s[j:][::-1]
        if ans > a:
            ans = a
print(ans)
