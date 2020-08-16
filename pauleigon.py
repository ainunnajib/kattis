s = input().split()
n = int(s[0])
r = int(s[1])+int(s[2])
t = int(r/n)
if t%2 == 0:
    print('paul')
else:
    print('opponent')