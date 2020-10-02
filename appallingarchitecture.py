h, w = map(int, input().split())
a = []
s = 0
c = 0
for _ in range(h):
    l = input()
    x = [(l[i] != '.')*(2*i+1) for i in range(w)]
    r = [l[i] != '.' for i in range(w)]
    if sum(r) > 0:
        s += sum(x)
        c += sum(r)
left = r.index(True)
right = w - (r[::-1].index(True))
left *= 2 * c
right *= 2 * c
if s < left:
    print('left')
elif s > right:
    print('right')
else:
    print('balanced')
