r, c = map(int, input().split())
a = [[0 for i in range(c+2)] for j in range(r+2)]
for j in range(1, r+1):
    s = input()
    for i in range(1, c+1):
        if s[i-1] == 'T':
            a[j][i] = 1
maxring = 0
for ring in range(1, 50):
    for j in range(1, r+1):
        for i in range(1, c+1):
            if ring == min(a[j-1][i], a[j+1][i], a[j][i-1], a[j][i+1]):
                a[j][i] = ring + 1
                maxring = max(maxring, ring+1)
if maxring < 10:
    template = ['.', '.']
else:
    template = ['.', '.', '.']
for row in a[1:-1]:
    s = ''
    for x in row[1:-1]:
        if x == 0:
            s += ''.join(template)
        elif x < 10:
            c = template.copy()
            c[-1] = str(x)
            s += ''.join(c)
        else:
            c = template.copy()
            c[-1] = str(x%10)
            c[-2] = str(x//10)
            s += ''.join(c)
    print(s)
