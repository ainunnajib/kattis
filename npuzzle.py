b = 'ABCDEFGHIJKLMNO.'
total = 0
for row in range(4):
    s = input()
    for column in range(4):
        if s[column] != '.':
            i = b.index(s[column])
            r = i//4
            c = i%4
            total += abs(row-r) + abs(column-c)
print(total)
