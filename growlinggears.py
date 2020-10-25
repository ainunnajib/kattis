t = int(input())
for _ in range(t):
    n = int(input())
    maxtorque = 0
    maxgear = 0
    for i in range(1, n+1):
        a, b, c = map(int, input().split())
        x = b/(2*a)
        torque = -1*a*x*x + b*x + c
        if torque > maxtorque:
            maxtorque = torque
            maxgear = i
    print(maxgear)
