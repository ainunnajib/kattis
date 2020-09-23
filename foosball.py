n = int(input())
p = input().split()
games = input()
lg = len(games)

w1 = p.pop(0)
b1 = p.pop(0)
w2 = p.pop(0)
b2 = p.pop(0)
w = (w1, w2)
b = (b1, b2)

streak = 0
prev = ''
dynasties = []

for i in range(lg):
    g = games[i]
    if g == prev:
        streak += 1
    else:
        if prev == 'W':
            dynasties.append((streak, -1*i, w1, w2))
        elif prev == 'B':
            dynasties.append((streak, -1*i, b1, b2))
        streak = 1
    prev = g

    if g == 'W':
        w = w[::-1]
        p.append(b[1])
        b = (p.pop(0), b[0])
        b2, b1 = b
    else:
        b = b[::-1]
        p.append(w[1])
        w = (p.pop(0), w[0])
        w2, w1 = w
if prev == 'W':
    dynasties.append((streak, -1*lg, w1, w2))
elif prev == 'B':
    dynasties.append((streak, -1*lg, b1, b2))

dynasties.sort(reverse = True)
maxstreak = dynasties[0][0]
for d in dynasties:
    if d[0] != maxstreak:
        break
    print(d[2], d[3])
