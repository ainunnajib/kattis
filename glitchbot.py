x, y = map(int, input().split())
n = int(input())
s = []
o = {'Forward':['Right', 'Left'], 'Right':['Forward', 'Left'], 'Left':['Forward', 'Right']}

for _ in range(n):
    s.append(input())

def step(cur, act):
    if act == 'Forward':
        cur[0] += cur[2]
        cur[1] += cur[3]
    elif act == 'Right':
        if cur[2] == 0:
            cur[2] = cur[3]
            cur[3] = 0
        else:
            cur[3] = -1*cur[2]
            cur[2] = 0
    elif act == 'Left':
        if cur[2] == 0:
            cur[2] = -1*cur[3]
            cur[3] = 0
        else:
            cur[3] = cur[2]
            cur[2] = 0

done = False
for i in range(n):
    c = [0, 0, 0, 1] # x, y, +x, +y
    for k in range(i):
        step(c, s[k])
    for j in range(2):
        b = c.copy() # backup to backtrack
        step(c, o[s[i]][j])
        for k in range(i+1, n):
            step(c, s[k])
        if c[0] == x and c[1] == y:
            print(i+1, o[s[i]][j])
            done = True
            break
        c = b
    if done:
        break
