days = {'SAT':0, 'SUN':1, 'MON':2, 'TUE':3, 'WED':4, 'THU':5, 'FRI':6}
months = {'JAN':0, 'FEB':1, 'MAR':2, 'APR':3, 'MAY':4, 'JUN':5,
          'JUL':6, 'AUG':7, 'SEP':8, 'OCT':9, 'NOV':10, 'DEC':11}
monthdays = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
monthdaysleap = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

s = input().split()
a = days[input()]

d = int(s[0]) - 1
m = months[s[1]]
x, y = 0, 0
for i in range(m):
    x += monthdays[i]
    y += monthdaysleap[i]
x += d
y += d
x += a
y += a
x %= 7
y %= 7
if x == 6 and y == 6:
    print('TGIF')
elif x == 6 or y == 6:
    print('not sure')
else:
    print(':(')
