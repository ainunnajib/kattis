t = int(input())
for _ in range(t):
    n = int(input())
    score = 0
    for __ in range(n):
        x, y = map(int, input().split())
        rr = x**2 + y**2

        if rr <= 20*20:
            score += 10
        elif rr <= 40*40:
            score += 9
        elif rr <= 60*60:
            score += 8
        elif rr <= 80*80:
            score += 7
        elif rr <= 100*100:
            score += 6
        elif rr <= 120*120:
            score += 5
        elif rr <= 140*140:
            score += 4
        elif rr <= 160*160:
            score += 3
        elif rr <= 180*180:
            score += 2
        elif rr <= 200*200:
            score += 1

    print(score)
