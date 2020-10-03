from collections import defaultdict
n, b = map(int, input().split())
l = list(map(int, input().split()))
ib = l.index(b)

ks = set()

left = defaultdict(int)
less = 0
for x in l[:ib][::-1]:
    if x < b:
        less += 1
    else:
        less -= 1
    left[less] += 1
    ks.add(less)

right = defaultdict(int)
more = 0
for x in l[ib+1:]:
    if x > b:
        more += 1
    else:
        more -= 1
    right[more] += 1
    ks.add(more)

count = 1 + left[0] + right[0]
for k in ks:
    count += left[k] * right[k]

print(count)
