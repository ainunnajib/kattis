l, w, n, r = map(int, input().split())
centres = [(0, w/2), (0, -1*w/2), (l/2, 0), (-1*l/2, 0)]

cranes = []
for _ in range(n):
    x, y = map(int, input().split())
    s = set()
    for i in range(4):
        p, q = centres[i]
        if (x-p)**2 + (y-q)**2 <= r**2:
            s.add(i)
    cranes.append(s)

done = False
if max([len(c) for c in cranes]) == 4:
    print(1)
    done = True

if not done:
    for i in range(n):
        for j in range(i+1, n):
            if len(cranes[i] | cranes[j]) == 4:
                print(2)
                done = True
                break
        if done:
            break

if not done:
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if len(cranes[i] | cranes[j] | cranes[k]) == 4:
                    print(3)
                    done = True
                    break
            if done:
                break
        if done:
            break

if not done:
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                for m in range(k+1, n):
                    if len(cranes[i] | cranes[j] | cranes[k] | cranes[m]) == 4:
                        print(4)
                        done = True
                        break
                if done:
                    break
            if done:
                break
        if done:
            break

if not done:
    print('Impossible')
