n = int(input())
i = 1
l = []
while i < n:
    l.append(str(i))
    i *= 2
print(len(l))
print(' '.join(l))
