year = int(input())
jan = ((year - 2018) * 12) % 26
dec = (jan + 11) % 26
if ((3 - jan) % 26 + (dec - 3) % 26) <= 12:
    print("yes")
else:
    print("no")
