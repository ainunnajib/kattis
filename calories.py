prev = ""
s = input()
total = 0
totalfat = 0
while prev != "-" or s != "-":
    if s != "-":
        perc = 0
        calories = 0
        totalcalories = 0
        values = []
        isperc = [False] * 5

        a = s.split()
        for i in range(5):
            unit = a[i][-1]
            value = int(a[i][:-1])
            if unit == '%':
                perc += value
                isperc[i] = True
            elif unit == 'C':
                calories += value
            elif unit == 'g':
                if i == 0:
                    value *= 9
                elif i > 0 and i < 4:
                    value *= 4
                else:
                    value *= 7
                calories += value
            values.append(value)
        totalcalories = 100*calories/(100-perc)
        for i in range(5):
            if isperc[i]:
                values[i] = totalcalories*values[i]/100
        total += totalcalories
        totalfat += values[0]
    else:
        # calculate & print the case result
        perc = round(100*totalfat/total)
        print(str(perc)+'%')
        total = 0
        totalfat = 0
    prev = s
    s = input()
