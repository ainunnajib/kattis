n = int(input())
score = 0
prev = ''
for _ in range(n):
    c = input()
    if prev == c:
        score += 1
    else:
        prev = c
print(score)