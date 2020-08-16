n = int(input())
for i in range(n):
    a = input()
    b = input()
    l = len(a)
    c = [ ('.' if a[j] == b[j] else '*') for j in range(l) ]
    print(a)
    print(b)
    print(''.join(c))
    print("")