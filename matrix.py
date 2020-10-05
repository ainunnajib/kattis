i = 0
while True:
    try:
        i += 1
        a, b = map(int, input().split())
        c, d = map(int, input().split())
        _ = input()
        print(f'Case {i}:')
        div = a*d - b*c
        print(d//div, -1*b//div)
        print(-1*c//div, a//div)
    except EOFError:
        break
