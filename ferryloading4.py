c = int(input())
for _ in range(c):
    l, m = map(int, input().split())
    l *= 100
    d = {'left':[], 'right':[]}
    for __ in range(m):
        s = input().split()
        d[s[1]].append(int(s[0]))
    left = 0
    cur = 0
    for x in d['left']:
        if cur + x > l:
            left += 1
            cur = x
        else:
            cur += x
    if cur > 0:
        left += 1

    right = 0
    cur = 0
    for x in d['right']:
        if cur + x > l:
            right += 1
            cur = x
        else:
            cur += x
    if cur > 0:
        right += 1

    if left > right:
        print(2*left - 1)
    elif left == right:
        print(2*left)
    elif right > left:
        print(2*right)
