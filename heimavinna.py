l = input().split(';')
total = 0
for s in l:
    if '-' in s:
        a, b = map(int, s.split('-'))
        total += b-a+1
    else:
        total += 1
print(total)