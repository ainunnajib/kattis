n = int(input())
for _ in range(n):
    plays, wins, draws, losses, points = input().split()
    d = {}
    if plays != '?':
        d['plays'] = int(plays)
    if wins != '?':
        d['wins'] = int(wins)
    if draws != '?':
        d['draws'] = int(draws)
    if losses != '?':
        d['losses'] = int(losses)
    if points != '?':
        d['points'] = int(points)

    if 'points' in d:
        if d['points'] < 3:
            d['draws'] = d['points']
            d['wins'] = 0
    if 'plays' in d:
        if d['plays'] == 0:
            d['wins'] = 0
            d['draws'] = 0
            d['losses'] = 0
            d['points'] = 0
        elif 'losses' in d:
            if d['plays'] == d['losses']:
                d['wins'] = 0
                d['draws'] = 0
                d['points'] = 0
    elif 'wins' in d or 'draws' in d or 'losses' in d:
        total = 0
        if 'wins' in d:
            total += d['wins']
        if 'draws' in d:
            total += d['draws']
        if 'losses' in d:
            total += d['losses']
        if total == 100:
            d['plays'] = 100
            if 'wins' not in d:
                d['wins'] = 0
            if 'draws' not in d:
                d['draws'] = 0
            if 'losses' not in d:
                d['losses'] = 0

    if 'wins' in d and 'draws' in d and 'losses' in d:
        d['plays'] = d['wins'] + d['draws'] + d['losses']
        d['points'] = 3*d['wins'] + d['draws']

    if 'plays' not in d:
        if 'wins' in d and 'draws' in d:
            if 'losses' not in d:
                d['losses'] = 0
            d['plays'] = d['wins'] + d['draws'] + d['losses']
        elif 'points' in d:
            if 'losses' not in d:
                d['losses'] = 0

            if 'wins' in d:
                d['plays'] = d['wins'] + (d['points'] - 3*d['wins']) + d['losses']
            elif 'draws' in d:
                d['plays'] = (d['points'] - d['draws'])//3 + d['draws'] + d['losses']

    if 'wins' not in d:
        if 'plays' in d:
            if 'draws' in d and 'losses' in d:
                d['wins'] = d['plays'] - d['draws'] - d['losses']

        if 'points' in d:
            if 'draws' in d:
                d['wins'] = (d['points'] - d['draws'])//3
            elif 'losses' in d:
                if 'plays' in d:
                    d['wins'] = (d['points'] - d['plays'] + d['losses'])//2
                else:
                    d['wins'] = d['points']//3
                    d['draws'] = d['points']%3
                    d['plays'] = d['wins'] + d['draws'] + d['losses']
            elif 'plays' in d:
                d['wins'] = d['points']//3
                d['draws'] = d['points']%3
                d['losses'] = d['plays'] - d['wins'] - d['draws']


    if 'draws' not in d:
        if 'plays' in d:
            if 'wins' in d and 'losses' in d:
                d['draws'] = d['plays'] - d['wins'] - d['losses']

        if 'points' in d:
            if 'wins' in d:
                d['draws'] = d['points'] - 3*d['wins']
            elif 'plays' in d:
                d['draws'] = (3*d['plays'] - d['points'] - 3*d['losses'])//2

    if 'losses' not in d:
        if 'plays' in d:
            if 'wins' in d and 'draws' in d:
                d['losses'] = d['plays'] - d['wins'] - d['draws']

    if 'points' not in d:
        if 'wins' in d and 'draws' in d:
            d['points'] = 3*d['wins'] + d['draws']


    print(d['plays'], d['wins'], d['draws'], d['losses'], d['points'])
