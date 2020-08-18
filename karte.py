s = input()
d = {'P':[0]*13, 'K':[0]*13, 'H':[0]*13, 'T':[0]*13}
for i in range(len(s)//3):
    x = s[i*3:i*3+3]
    a = x[0]
    n = int(x[1:])
    d[a][n-1] += 1
if max(d['P']) > 1 or max(d['K']) > 1 or max(d['H']) > 1 or max(d['T']) > 1:
    print("GRESKA")
else:
    print(13-sum(d['P']), 13-sum(d['K']), 13-sum(d['H']), 13-sum(d['T']))
