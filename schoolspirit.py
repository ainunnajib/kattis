n = int(input())
s = []
for _ in range(n):
    s.append(int(input()))
s.sort(reverse = True)
groupscore = 0.0
for i in range(n):
    groupscore += s[i] * (0.8 ** i)
groupscore /= 5
print(groupscore)
g = []
for i in range(n):
    score = 0.0
    for j in range(n):
        if j < i:
            score += s[j] * (0.8 ** j)
        elif j > i:
            score += s[j] * (0.8 ** (j-1))
    score /= 5
    g.append(score)
print(sum(g)/len(g))
