t = int(input())
for i in range(t):
    s = input()
    ng, nm = map(int, input().split())
    g = list(map(int, input().split()))
    m = list(map(int, input().split()))
    g.sort()
    m.sort()
    if g[-1] >= m[-1]:
        print("Godzilla")
    else:
        print("MechaGodzilla")
