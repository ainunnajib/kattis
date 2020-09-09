n, y = map(int, input().split())
o = [True for i in range(n)]
for _ in range(y):
    o[int(input())] = False
for i in range(n):
    if o[i]:
        print(i)
print(f'Mario got {n-sum(o)} of the dangerous obstacles.')
