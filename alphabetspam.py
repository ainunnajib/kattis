s = input()
denum = len(s)
whitespace = 0
lowercase = 0
uppercase = 0
symbol = 0
for c in s:
    if c in "abcdefghijklmnopqrstuvwxyz":
        lowercase += 1
    elif c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        uppercase += 1
    elif c == '_':
        whitespace += 1
    else:
        symbol += 1
print(1.0*whitespace/denum)
print(1.0*lowercase/denum)
print(1.0*uppercase/denum)
print(1.0*symbol/denum)