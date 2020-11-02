r = int(input())
s = list(input())
n = int(input())
l = []

score = 0
for _ in range(n):
    x = list(input())
    for i in range(r):
        if s[i] == x[i]:
            score += 1
        elif (s[i], x[i]) in {('S', 'P'), ('P', 'R'), ('R', 'S')}:
            score += 2
    l.append(x)
print(score)

maxscore = 0
lr = [[l[i][j] for i in range(n)] for j in range(r)]
for x in lr:
    ss = x.count('S')
    pp = x.count('P')
    rr = x.count('R')
    maxscore += max(2*ss + rr, 2*rr + pp, 2*pp + ss)
print(maxscore)
