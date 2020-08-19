t = int(input())
for _ in range(t):
    w, h, n = map(int, input().split())
    maps = [ [False] * (w*h), [False] * (w*h) ]
    for y in range(h-1,-1,-1):
        s = input()
        for x in range(w):
            maps[0][y*w + x] = s[x] == '#'
    for y in range(h-1,-1,-1):
        s = input()
        for x in range(w):
            maps[1][y*w + x] = s[x] == '#'

    win = ""
    if sum(maps[0]) == 0 and sum(maps[1]) == 0:
        win = "draw"
    elif sum(maps[0]) == 0:
        win = "two"
    elif sum(maps[1]) == 0:
        win = "one"

    end = False
    turn = 0 # 0 = player one, 1 = player two
    for i in range(n):
        x, y = map(int, input().split())
        if end:
            continue

        if maps[1-turn][y*w + x]: # hit a ship
            maps[1-turn][y*w + x] = False
            # check if finished
            if sum(maps[1-turn]) == 0:
                if turn == 0:
                    # give player two one last turn
                    win = "one"
                    turn = 1-turn
                else:
                    if win == "":
                        win = "two"
                    else:
                        win = "draw"
                    end = True
        else:
            if sum(maps[1]) == 0:
                win = "one"
                end = True
            turn = 1-turn

    if win == "draw" or win == "":
        print("draw")
    else:
        print("player", win, "wins")
