n = int(input())
for i in range(n):
    m = int(input())
    l = input().split()
    num = [ int(x) for x in l ]
    print(int((max(num)-min(num))*2))