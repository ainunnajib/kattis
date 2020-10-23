from sys import stdin, stdout
line = stdin.readline()
while line != '':
    n = int(line.split('/')[1])
    ways = 0
    x = n + 1
    y = x
    while True:
        if (x*n) % (x-n) == 0:
            y = x * n / (x - n)
            if x <= y:
                ways += 1
            else:
                break
        if x > y:
            break
        x += 1

    stdout.write(str(ways) + '\n')

    line = stdin.readline()
