import sys
l = []
for line in sys.stdin.readlines():
    l.append(len(line.strip()))
m = max(l)
score = 0
for n in l[:-1]:
    score += (m-n)**2
print(score)
