line = input().split()
hh = int(line[0])
mm = int(line[1])
mm -= 45
if mm < 0:
    mm += 60
    hh -= 1
    if hh < 0:
        hh += 24
print(str(hh) + " " + str(mm))