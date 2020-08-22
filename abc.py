s = sorted(list(map(int, input().split())))
x = input()
d = {'A':0, 'B':1, 'C':2}
print(s[d[x[0]]], s[d[x[1]]], s[d[x[2]]])
