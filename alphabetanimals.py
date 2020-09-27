from collections import defaultdict

s = input()
n = int(input())

l = []
starts = defaultdict(set)
ends = defaultdict(set)
for i in range(n):
    a = input()
    l.append(a)
    start, end = a[0], a[-1]
    starts[start].add(i)
    ends[end].add(i)

end = s[-1]
if end not in starts:
    print('?')
else:
    done = False
    valid = '?'
    for i in starts[end]:
        e = l[i][-1]
        if len(starts[e]) == 0 or (len(starts[e]) == 1 and i in starts[e]):
            print(l[i]+'!')
            done = True
            break
        elif valid == '?':
            valid = l[i]
    if not done:
        print(valid)
