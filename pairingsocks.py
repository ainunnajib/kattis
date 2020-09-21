n = int(input())
a = list(map(int, input().split()))[::-1]
b = []
moves = 0
while len(a) > 0:
    if len(b) > 0 and b[-1] == a[-1]:
        a.pop()
        b.pop()
    else:
        b.append(a.pop())
    moves += 1
if len(b) > 0:
    print('impossible')
else:
    print(moves)
