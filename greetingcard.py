d = set()
n = int(input())
for _ in range(n):
    x, y = map(int, input().split())
    d.add((x, y))
pairs = 0
for t in d:
    x, y = t
    if (x+2018, y) in d:
        pairs += 1
    if (x-2018, y) in d:
        pairs += 1
    if (x, y+2018) in d:
        pairs += 1
    if (x, y-2018) in d:
        pairs += 1

    if (x+1118, y+1680) in d:
        pairs += 1
    if (x-1118, y-1680) in d:
        pairs += 1
    if (x+1118, y-1680) in d:
        pairs += 1
    if (x-1118, y+1680) in d:
        pairs += 1

    if (x+1680, y+1118) in d:
        pairs += 1
    if (x-1680, y-1118) in d:
        pairs += 1
    if (x+1680, y-1118) in d:
        pairs += 1
    if (x-1680, y+1118) in d:
        pairs += 1

print(pairs//2)
