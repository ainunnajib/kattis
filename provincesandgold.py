l = input().split()
g = int(l[0])
s = int(l[1])
c = int(l[2])
buy = 3*g + 2*s + c
if buy >= 8:
    v = "Province"
elif buy >= 5:
    v = "Duchy"
elif buy >= 2:
    v = "Estate"
else:
    v = ""
if buy >= 6:
    t = "Gold"
elif buy >= 3:
    t = "Silver"
else:
    t = "Copper"
if v == "":
    print(t)
else:
    print(v + " or " + t)