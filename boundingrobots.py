w, l = map(int, input().split())
while not (w == 0 and l == 0):
    actualx, actualy, robotx, roboty = 0, 0, 0, 0
    n = int(input())
    for _ in range(n):
        move, dist = input().split()
        dist = int(dist)
        if move == "u":
            roboty += dist
            actualy = min(l - 1, actualy + dist)
        elif move == "d":
            roboty -= dist
            actualy = max(0, actualy - dist)
        elif move == "l":
            robotx -= dist
            actualx = max(0, actualx - dist)
        elif move == "r":
            robotx += dist
            actualx = min(w - 1, actualx + dist)
    print("Robot thinks", robotx, roboty)
    print("Actually at", actualx, actualy)
    print("")
    w, l = map(int, input().split())
