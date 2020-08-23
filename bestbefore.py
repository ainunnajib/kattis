s = input()
a, b, c = map(int, s.split('/'))
# [] of day, month, year
days   = [a, a, b, b, c, c]
months = [b, c, a, c, a, b]
years  = [c, b, c, a, b, a]
valid = False
resultyear, resultmonth, resultday = 9999, 9999, 9999

for i in range(6):
    day = days[i]
    month = months[i]
    year = years[i]

    if day == 0 or month == 0:
        continue

    if day > 31:
        continue

    if month > 12:
        continue

    if day == 31 and month in [2, 4, 6, 9, 11]:
        continue

    if day == 30 and month == 2:
        continue

    if year < 100:
        year += 2000

    isleapyear = (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0))

    if day == 29 and month == 2 and not isleapyear:
        continue

    valid = True
    if resultyear > year or (resultyear == year and resultmonth > month) or (resultyear == year and resultmonth == month and resultday > day):
        resultyear = year
        resultmonth = month
        resultday = day
        result = str(resultyear) + '-' + ('0' if resultmonth < 10 else '') + str(resultmonth) + '-' + ('0' if resultday < 10 else '') + str(resultday)

if not valid:
    print(s, "is illegal")
else:
    print(result)
