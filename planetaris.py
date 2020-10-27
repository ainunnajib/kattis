n, a = map(int, input().split())
l = list(map(int, input().split()))
l.sort()
wins = 0
for x in l:
    if a > x:
        a -= x+1
        wins += 1
    else:
        break
print(wins)
