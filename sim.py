import sys
t = int(sys.stdin.readline())
for line in sys.stdin.readlines():
#for _ in range(t):
    a, b = [], []
    #for c in sys.stdin.readline().strip():
    for c in line.strip():
        if c == '[':
            a.extend(b)
            b = a
            a = []
        elif c == ']':
            a.extend(b)
            b = []
        elif c == '<':
            if len(a) > 0:
                a.pop(-1)
        else:
            a.append(c)
    print(''.join(a+b))
