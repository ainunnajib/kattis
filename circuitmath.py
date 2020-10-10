az = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

n = int(input())
l = [c == 'T' for c in input().split()]

o = []
s = input().split()
for c in s:
    if c in az:
        o.append(l[az.index(c)])
    else:
        if c == '*':
            x = o.pop()
            y = o.pop()
            o.append(x and y)
        elif c == '+':
            x = o.pop()
            y = o.pop()
            o.append(x or y)
        elif c == '-':
            x = o.pop()
            o.append(not x)

print('T' if o[0] else 'F')
