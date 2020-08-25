s = input().split()
a = s[0]
b = s[1]
for x in a:
    if x in b:
        j = b.index(x)
        i = a.index(x)
        break
for n in range(len(b)):
    if n == j:
        row = a
    else:
        row = ""
        for m in range(len(a)):
            if m == i:
                row += b[n]
            else:
                row += '.'
    print(row)
