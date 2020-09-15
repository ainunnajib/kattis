s = input()
l = len(s)
minchar = l
for i in range(l):
    for j in range(2, l+1):
        m = s[i:i+j]
        c = l + j
        k = 0
        while k < l:
            if s[k:k+j] == m:
                c -= j
                c += 1
                k += j
            else:
                k += 1
        minchar = min(minchar, c)
print(minchar)
