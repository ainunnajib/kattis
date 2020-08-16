s = input()
a = []
for c in s:
    if c == '<':
        a.pop()
    else:
        a.append(c)
print(''.join(a))