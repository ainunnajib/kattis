a, b = map(int, input().split())
i = 0
done = False
while a != b:
    if a < b:
        print(i + b-a)
        done = True
        break
    elif a%2 == 1:
        a += 1
    elif a%2 == 0:
        a //= 2
    i += 1
if not done:
    print(i)