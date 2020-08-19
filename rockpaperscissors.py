s = input()
while s != "0":
    n, k = map(int, s.split())
    wins = [0]*n
    losses = [0]*n
    for _ in range(k*n*(n-1)//2):
        s = input().split()
        p1 = int(s[0])-1
        m1 = s[1]
        p2 = int(s[2])-1
        m2 = s[3]
        if m1 != m2:
            if (m1 == "rock" and m2 == "scissors") or (m1 == "scissors" and m2 == "paper") or (m1 == "paper" and m2 == "rock"):
                wins[p1] += 1
                losses[p2] += 1
            elif (m1 == "rock" and m2 == "paper") or (m1 == "paper" and m2 == "scissors") or (m1 == "scissors" and m2 == "rock"):
                losses[p1] += 1
                wins[p2] += 1
    for i in range(n):
        if wins[i]+losses[i] > 0:
            ans = round(1.0*wins[i]/(wins[i]+losses[i]), 3)
            print("{:.3f}".format(ans))
        else:
            print("-")
    s = input()
    if s != "0":
        print()
