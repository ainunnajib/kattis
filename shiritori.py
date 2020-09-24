d = set()
n = int(input())
l = []
for i in range(n):
    l.append(input())

fair = True
d.add(l[0])
for i in range(1, n):
    if l[i][0] != l[i-1][-1] or l[i] in d:
        fair = False
        print('Player', i%2+1, 'lost')
        break
    d.add(l[i])
if fair:
    print('Fair Game')
