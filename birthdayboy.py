n = int(input())

calendar = [False] * 365
monthdays = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
adddays = [0] * 12

for i in range(1, 12):
    for j in range(i, 12):
        adddays[j] += monthdays[i-1]

for _ in range(n):
    s = input().split()
    month = int(s[1].split('-')[0]) - 1
    day = adddays[month] + int(s[1].split('-')[1]) - 1
    calendar[day] = True

j = 299 # current date 27 Oct
while not calendar[j]:
    j -= 1
    j %= 365
# now calendar[j] is True, meaning, the previous birthday today or earlier
gap = 0
bestgap = 0
for i in range(j, j+365+365):
    if not calendar[i%365]:
        gap += 1
        if gap > bestgap:
            bestgap = gap
            bestday = i%365
        elif gap == bestgap:
            if (i%365 - 300)%365 < (bestday - 300)%365:
                bestday = i%365
    else:
        gap = 0

bestmonth = 0
while bestday - monthdays[bestmonth] >= 0:
    bestday -= monthdays[bestmonth]
    bestmonth += 1
bestmonth += 1
bestday += 1

print(('0' if bestmonth < 10 else '') + str(bestmonth) + '-' + ('0' if bestday < 10 else '') + str(bestday))
