n = int(input())
for i in range(n):
    s = input().split()
    g = [ int(x) for x in s ]
    if g[0] < 3:
        print(1)
        continue
    for i in range(2,len(g)-1):
        if g[i] != g[i+1]-1 and g[i] != g[i-1]+1:
            print(i)
            break