n = int(input())
prev = 1
for _ in range(n):
    a, o, b = input().split()
    a, b = int(a), int(b)
    if o == '*':
        r = a*a*b*b
    elif o == '+':
        r = a+b - prev
    elif o == '-':
        r = (a-b)*prev
    elif o == '/':
        r = (a+1)//2
    print(r)
    prev = r