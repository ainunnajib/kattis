import math
actions = [0 for i in range(43201)]
n = int(input())
for _ in range(n):
    d, t = map(int, input().split())
    actions[t] += 1
    actions[t-d] += 1
    actions[t-2*d] += 1
print(math.ceil(max(actions)/2))
