import sys
shares = 0.0
totalcost = 0.0
cost = 0.0
for s in sys.stdin.readlines():
    a = s.split()
    act = a[0]
    x = int(a[1])
    if act in ["buy", "sell"]:
        y = int(a[2])
    if act == "buy":
        shares += x
        totalcost += x*y
        cost = 1.0*totalcost/shares
    elif act == "sell":
        shares -= x
        totalcost -= cost*x
    elif act == "split":
        shares *= x
        cost /= x
    elif act == "merge":
        sold = shares%x
        shares = int(shares/x)
        cost *= x
        totalcost = cost*shares
    elif act == "die":
        if x < cost:
            coeff = 1.0
        else:
            coeff = 0.7
        print(coeff*(x-cost)*shares + cost*shares)
