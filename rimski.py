s = input()
d = {'I':0, 'V':0, 'X':0, 'L':0, 'C':0}
for x in s:
    d[x] += 1
tens = ""
unit = ""
# minimize tens first
if d['C'] == 1:
    if d['X'] == 1:
        tens = "XC"
        d['C'] -= 1
        d['X'] -= 1
    elif d['X'] == 2 and d['I'] == 1:
        tens = "XC"
        unit = "IX"
        d['C'] -= 1
        d['X'] -= 2
        d['I'] -= 1
elif d['L'] == 1:
    tens = "L"
    d['L'] -= 1
    if d['X'] == 0:
        pass
    elif d['X'] == 1:
        tens = "XL"
        d['X'] -= 1
    elif d['X'] == 2:
        if d['I'] == 1 and d['V'] == 0:
            tens = "XL"
            unit = "IX"
            d['X'] -= 2
            d['I'] -= 1
        else:
            tens = "LXX"
            d['X'] -= 2
    elif d['X'] == 3:
        if d['I'] == 1 and d['V'] == 0:
            tens = "LXX"
            unit = "IX"
            d['X'] -= 3
            d['I'] -= 1
        else:
            tens = "LXXX"
            d['X'] -= 3
    elif d['X'] == 4:
        if d['I'] == 1 and d['V'] == 0:
            tens = "LXXX"
            unit = "IX"
            d['X'] -= 4
            d['I'] -= 1
        else:
            pass #impossible
elif d['X'] == 4:
    if d['I'] == 1 and d['V'] == 0:
        tens = "XXX"
        unit = "IX"
        d['X'] -= 4
        d['I'] -= 1
    else:
        pass #impossible
elif d['X'] == 3:
    if d['I'] == 1 and d['V'] == 0:
        tens = "XX"
        unit = "IX"
        d['X'] -= 3
        d['I'] -= 1
    else:
        tens = "XXX"
        d['X'] -= 3
elif d['X'] == 2:
    if d['I'] == 1 and d['V'] == 0:
        tens = "X"
        unit = "IX"
        d['X'] -= 2
        d['I'] -= 1
    else:
        tens = "XX"
        d['X'] -= 2
elif d['X'] == 1:
    if d['I'] == 1 and d['V'] == 0:
        tens = ""
        unit = "IX"
        d['X'] -= 1
        d['I'] -= 1
    else:
        tens = "X"
        d['X'] -= 1

# unit is left
if unit == "":
    if d['V'] == 1:
        if d['I'] == 1:
            unit = "IV"
            d['V'] -= 1
            d['I'] -= 1
        else:
            unit = "V"
            d['V'] -= 1
            while d['I'] > 0:
                unit += 'I'
                d['I'] -= 1
    else:
        while d['I'] > 0:
            unit += 'I'
            d['I'] -= 1

print(tens+unit)
if d['C'] + d['L'] + d['X'] + d['V'] + d['I'] > 0:
    print("impossible")
