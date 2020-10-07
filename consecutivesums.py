t = int(input())
for _ in range(t):
    n = int(input())
    if n % 2 == 1:
        if n == 1:
            print('IMPOSSIBLE')
        else:
            print(f'{n} = {(n-1)//2} + {(n+1)//2}')
        continue

    done = False
    num = 3
    while num*(num+1)/2 <= n:
        sum = num*(num+1)//2
        if (n - sum) % num == 0:
            x = (n - sum) // num
            k = x + 1
            if k > 0:
                s = str(n) + ' = ' + str(k)
                for i in range(k+1, k+num):
                    s += ' + ' + str(i)
                print(s)
                done = True
                break

        num += 1

    if not done:
        print('IMPOSSIBLE')
