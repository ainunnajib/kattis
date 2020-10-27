n = int(input())
for case in range(1, n+1):
    p, k, l = map(int, input().split())
    ls = list(map(int, input().split()))
    ls.sort(reverse = True)

    i = 0
    count = 0
    done = False
    for press in range(1, p+1):
        for key in range(1, k+1):
            count += ls[i] * press
            i += 1
            if i == l:
                done = True
                break
        if done:
            break

    print(f'Case #{case}: {count}')
