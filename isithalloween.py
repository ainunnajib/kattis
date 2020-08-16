l = input().split()
mon = l[0]
day = int(l[1])
if (mon == "OCT" and day == 31) or (mon == "DEC" and day == 25):
    print("yup")
else:
    print("nope")