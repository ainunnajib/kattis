x, y = map(int, input().split())

if y == 0:
    if x <= 125:
        b = 250.0*125/(250-x)
        a = 250.0-b
        print("{:.2f}".format(round(a, 2)), "{:.2f}".format(round(b, 2)))
    else:
        b = 250.0*125/x
        print("0.00", "{:.2f}".format(round(b, 2)))
elif x == 0:
    if y <= 125:
        a = 250.0*125/(250-y)
        b = 250.0-a
        print("{:.2f}".format(round(a, 2)), "{:.2f}".format(round(b, 2)))
    else:
        a = 250.0*125/y
        print("{:.2f}".format(round(a, 2)), "0.00")
else:
    if x <= 125:
        a = 250.0 - 250.0*125/y
        print("{:.2f}".format(round(a, 2)), "0.00")
    else:
        b = 250.0 - 250.0*125/x
        print("0.00", "{:.2f}".format(round(b, 2)))
