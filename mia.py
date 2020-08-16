def score(a, b):
    if (a == 1 and b == 2) or (a == 2 and b == 1):
        return 0
    if a == b:
        return 7-a
    return 72 - 10*max(a,b) - min(a,b)

s = input()
while s != "0 0 0 0":
    s0, s1, r0, r1 = map(int, s.split())
    p1 = score(s0,s1)
    p2 = score(r0,r1)
    if p1 < p2:
        print("Player 1 wins.")
    elif p2 < p1:
        print("Player 2 wins.")
    else:
        print("Tie.")
    s = input()
