t = int(input())
for _ in range(t):
    n = int(input())
    votes = []
    for __ in range(n):
        votes.append(int(input()))
    winner = votes.index(max(votes)) + 1
    votes.sort()
    if votes[-1] == votes[-2]:
        print("no winner")
    elif votes[-1]*2 > sum(votes):
        print("majority winner", winner)
    else:
        print("minority winner", winner)
