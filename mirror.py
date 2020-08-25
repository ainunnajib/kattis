t = int(input())
for i in range(t):
    r, c = map(int, input().split())
    a = []
    for _ in range(r):
        a.append(input())
    print("Test", i+1)
    for j in range(r-1,-1,-1):
        print(a[j][::-1])
