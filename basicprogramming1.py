n, t = map(int, input().split())
a = list(map(int, input().split()))
if t == 1:
    print(7)
elif t == 2:
    if a[0] > a[1]:
        print("Bigger")
    elif a[0] == a[1]:
        print("Equal")
    else:
        print("Smaller")
elif t == 3:
    x = sorted(a[:3])
    print(x[1])
elif t == 4:
    print(sum(a))
elif t == 5:
    print(sum([x for x in a if x%2==0]))
elif t == 6:
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    a = [x%26 for x in a]
    s = [alphabet[x] for x in a]
    print("".join(s))
elif t == 7:
    i = 0
    steps = 0
    while steps <= n+1:
        i = a[i]
        steps += 1
        if i == n-1:
            print("Done")
            break
        elif i < 0 or i >= n:
            print("Out")
            break
        elif steps == n:
            print("Cyclic")
            break
