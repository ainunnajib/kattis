n = int(input())
for _ in range(n):
    street = input()
    addresses = input()
    k = addresses.split()[0]
    k = int(k)
    l = []
    while k > 0:
        s = input()
        if s[0] == '+':
            start, end, step = map(int, s[2:].split())
            while start <= end:
                l.append(str(start))
                k -= 1
                start += step
        else:
            l.append(s)
            k -= 1

    print(street)
    print(addresses)

    count = [0 for i in range(10)]
    for number in l:
        for digit in number:
            count[int(digit)] += 1

    for i in range(10):
        print('Make', count[i], 'digit', i)
    print('In total', sum(count), ('digits' if sum(count) > 1 else 'digit'))
