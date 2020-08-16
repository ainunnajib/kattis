from collections import defaultdict
inside = defaultdict(bool)
anomaly = ' (ANOMALY)'
n = int(input())
for i in range(n):
    s = input().split()
    if s[0] == 'entry':
        if (inside[s[1]]):
            print(s[1] + ' entered' + anomaly)
        else:
            print(s[1] + ' entered')
        inside[s[1]] = True
    else:
        if (inside[s[1]]):
            print(s[1] + ' exited')
        else:
            print(s[1] + ' exited' + anomaly)
        inside[s[1]] = False