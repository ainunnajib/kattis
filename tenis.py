players = input().split()
n = int(input())
for _ in range(n):
    possible = True
    wins = [0, 0]

    sets = input().split()
    if len(sets) > 3 or len(sets) < 2:
        possible = False
    else:
        for set in sets[:2]:
            scores = list(map(int, set.split(':')))
            if scores[0] > scores[1]:
                wins[0] += 1
            elif scores[1] > scores[0]:
                wins[1] += 1
            else:
                possible = False

            winscore = max(scores)
            losescore = min(scores)
            lead = winscore - losescore

            if winscore < 6:
                possible = False
            elif winscore == 6:
                if lead < 2:
                    possible = False
            elif winscore > 7:
                possible = False
            else: # winscore = 7
                if losescore < 5:
                    possible = False

        if len(sets) == 3:
            set = sets[2]
            scores = list(map(int, set.split(':')))
            if scores[0] > scores[1]:
                wins[0] += 1
            elif scores[1] > scores[0]:
                wins[1] += 1
            else:
                possible = False

            winscore = max(scores)
            losescore = min(scores)
            lead = winscore - losescore

            if winscore < 6:
                possible = False
            elif winscore == 6:
                if lead < 2:
                    possible = False
            else: # winscore >= 7
                if lead != 2:
                    possible = False

        if max(wins[0], wins[1]) != 2:
            possible = False

        if (players[0] == 'federer' and wins[1] > 0) or (players[1] == 'federer' and wins[0] > 0):
            possible = False

    if possible:
        print('da')
    else:
        print('ne')
