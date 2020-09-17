n = int(input())
p = []
for i in range(1, n+1):
    p.append(float(input().split()[1]))
p.sort(reverse = True)
print(sum([(i+1)*p[i] for i in range(n)]))
