n, a, b = input().split()
k = 2
i = 0
for c in a[::-1]:
    if c == '1':
        i = k - 1 - i
    k *= 2
k = 2
j = 0
for c in b[::-1]:
    if c == '1':
        j = k - 1 - j
    k *= 2
print(j-i-1)
