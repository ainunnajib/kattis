import math
from collections import defaultdict

def distance(a, b, c, d):
    return math.sqrt((a-c)**2 + (b-d)**2)

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
n, h, w = map(int, input().split())
while n != 0 or h != 0 or w != 0:

    forest = []
    for i in range(h):
        forest.append(list(input()))

    mills = {}
    for y in range(h):
        for x in range(w):
            if forest[y][x] in alphabet:
                mills[forest[y][x]] = (x, y)

    dist = {}
    for k in mills:
        dist[k] = [[999.9 for i in range(w)] for j in range(h)]
        x, y = mills[k]
        for j in range(h):
            for i in range(w):
                if forest[j][i] == '!':
                    dist[k][j][i] = distance(x, y, i, j)

    lumber = {}
    for k in mills:
        lumber[k] = 0.0

    for t in range(n):
        target = {}
        for k in mills:
            target[k] = (-1, -1)
            curdist = 888.8
            for j in range(h):
                for i in range(w):
                    if (dist[k][j][i] < curdist) or (dist[k][j][i] == curdist and i > target[k][0]) or (dist[k][j][i] == curdist and i == target[k][0] and j > target[k][1]):
                        curdist = dist[k][j][i]
                        target[k] = (i, j)

        count = defaultdict(int)
        for tree in target.values():
            if tree != (-1, -1):
                count[tree] += 1
                forest[tree[1]][tree[0]] = '.'
        for k in mills:
            for tree in target.values():
                dist[k][tree[1]][tree[0]] = 999.9

        for k in mills:
            if k in target and count[target[k]] > 0:
                lumber[k] += 1.0/count[target[k]]

    for j in range(h):
        print(''.join(forest[j]))
    for k in sorted(mills):
        print(k, lumber[k])

    n, h, w = map(int, input().split())
