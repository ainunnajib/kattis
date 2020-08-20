s = input().split()
value = int(s[0])
unit = s[1]
unitto = s[3]
u = ['th', 'in', 'ft', 'yd', 'ch', 'fur', 'mi', 'lea']
d = {'thou':'th', 'inch':'in', 'foot':'ft', 'yard':'yd', 'chain':'ch', 'furlong':'fur', 'mile':'mi', 'league':'lea'}
r = [1, 1000, 12, 3, 22, 10, 8, 3]
if unit not in u:
    unit = d[unit]
if unitto not in u:
    unitto = d[unitto]
i = u.index(unit)
j = u.index(unitto)
th = value
for x in range(i+1):
    value *= r[x]
for x in range(j+1):
    value /= r[x]
print(value)
