n = int(input())
p = list(map(int, input().split()))
p.sort(reverse = True)
print(sum(p[2::3]))
