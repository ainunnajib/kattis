a = list(map(int, input().split(':')))
b = list(map(int, input().split(':')))
x = a[0]*60*60 + a[1]*60 + a[2]
y = b[0]*60*60 + b[1]*60 + b[2]
d = (y-x) % (24*60*60)
if d == 0:
    d = 24*60*60
h = d // (60*60)
m = (d % (60*60)) // 60
s = d % 60
hh = ('0' if h < 10 else '') + str(h)
mm = ('0' if m < 10 else '') + str(m)
ss = ('0' if s < 10 else '') + str(s)
print(hh + ':' + mm + ':' + ss)
