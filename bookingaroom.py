r, n = map(int, input().split())
if r == n:
    print('too late')
else:
    rooms = []
    for _ in range(n):
        rooms.append(int(input()))
    for i in range(1, r+1):
        if i not in rooms:
            print(i)
            break
