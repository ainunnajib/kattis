capacity, lossrate, miles = map(float, input().split())
possible = False
answer = 0
for _ in range(6):
    speed, fuelefficiency = map(float, input().split())
    hours = miles/speed
    gallons = miles/fuelefficiency
    loss = lossrate*hours
    if gallons + loss <= capacity/2:
        possible = True
        answer = max(answer, speed)
if possible:
    print("YES", int(answer))
else:
    print("NO")
