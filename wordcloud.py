import math
t = 0
s = input()
while s != '0 0':
    t += 1
    w, n = map(int, s.split())
    words = []
    lengths = []
    freqs = []
    for i in range(n):
        a = input().split()
        words.append(a[0])
        lengths.append(len(a[0]))
        freqs.append(int(a[1]))
    maxfreq = max(freqs)

    heighttotal = 0
    heightrow = 0
    widthrow = 0
    for i in range(n):
        p = 8 + math.ceil(40*(freqs[i]-4)/(maxfreq-4))
        width = math.ceil(9*lengths[i]*p/16)

        if widthrow + width + 10 > w and widthrow > 0:
            heighttotal += heightrow
            heightrow = 0
            widthrow = 0
            firstline = False

        if widthrow == 0:
            widthrow = width
        elif widthrow + width + 10 == w:
            widthrow += width + 10
        else:
            widthrow += width + 10
        heightrow = max(heightrow, p)

    if widthrow != 0:
        heighttotal += heightrow

    print("CLOUD", str(t)+':', heighttotal)

    s = input()
