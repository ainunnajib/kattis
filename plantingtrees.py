n = int(input())
l = input().split()
t = [ int(x) for x in l ]
t.sort()
for i in range(n):
    t[i] += n-i
print(int(max(t))+1)