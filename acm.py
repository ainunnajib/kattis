correct = 0
score = 0

s = input()
while s != "-1":
    a = s.split()
    if a[2] == "right":
        correct += 1
        score += int(a[0])
    else:
        score += 20
    s = input()
