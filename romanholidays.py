romans = []
for i in range(1, 1001):
    s = i
    r = ""
    if s >= 1000:
        r = "M"
        s -= 1000
    elif s >= 900:
        r = "CM"
        s -= 900
    elif s >= 500:
        r = "D"
        s -= 500
    elif s >= 400:
        r = "CD"
        s -= 400
    while s >= 100:
        r += 'C'
        s -= 100

    if s >= 90:
        r += "XC"
        s -= 90
    elif s >= 50:
        r += "L"
        s -= 50
    elif s >= 40:
        r += "XL"
        s -= 40
    while s >= 10:
        r += "X"
        s -= 10

    if s == 9:
        r += "IX"
        s -= 9
    elif s >= 5:
        r += "V"
        s -= 5
    elif s == 4:
        r += "IV"
        s -= 4
    while s > 0:
        r += 'I'
        s -= 1

    romans.append(r)
romansorted = sorted(romans)

n = int(input())
for _ in range(n):
    k = int(input())
    thousands = k // 1000
    k = k % 1000

    roman = romans[k-1]
    position = romansorted.index(roman)+1
    if thousands > 0:
        pass # what to do?
