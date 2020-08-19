s = input()
stars = 0
combo = 0
rank = 25
req = [0,5,5,5,5,5,5,5,5,5,5,4,4,4,4,4,3,3,3,3,3,2,2,2,2,2]
for c in s:
    if c == 'W':
        stars += 1
        combo += 1
        if combo > 2 and rank >= 6 and rank <= 25:
            stars += 1
        if stars > req[rank] and rank > 0:
            stars -= req[rank]
            rank -= 1
    elif c == 'L':
        combo = 0
        if rank >= 1 and rank <= 20:
            if stars == 0 and rank == 20:
                pass
            elif stars == 0:
                rank += 1
                stars = req[rank] - 1
            elif stars > 0:
                stars -= 1
    if rank == 0:
        break
print("Legend" if rank == 0 else rank)
