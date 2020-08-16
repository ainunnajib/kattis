secret = input()
permute = input()
d = {}
for c in secret:
    d[c] = 1
wrong = 0
correct = 0
while wrong < 10 and correct < len(d):
    for c in permute:
        if c not in secret:
            wrong += 1
            if wrong > 9:
                break
        else:
            correct += 1
            if correct == len(d):
                break
if wrong < 10:
    print('WIN')
else:
    print('LOSE')
