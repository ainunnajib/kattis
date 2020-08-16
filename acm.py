from collections import defaultdict
problems = defaultdict(int)
correct = 0
score = 0

s = input()
while s != "-1":
    a = s.split()
    if a[2] == "right":
        correct += 1
        score += int(a[0]) + problems[a[1]]
    else:
        problems[a[1]] += 20
    s = input()
print(str(correct) + " " + str(score))
