from collections import defaultdict
t = int(input())
for _ in range(t):
    d = defaultdict(list)
    n = int(input())
    for __ in range(n):
        s = input().split()
        p = s[0][:-1]
        c = s[1].split('-')[::-1]
        score = 0
        for i in range(10):
            score *= 3
            if i < len(c):
                x = c[i]
                if x == 'upper':
                    score += 2
                elif x == 'middle':
                    score += 1
            else:
                score += 1
        d[score].append(p)

    for score in sorted(d.keys(), reverse = True):
        for p in sorted(d[score]):
            print(p)
    print('==============================')
