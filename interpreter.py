registers = [0 for i in range(10)]
rams = [0 for i in range(1000)]
i = 0
while True:
    try:
        rams[i] = int(input())
        i += 1
    except EOFError:
        break

count = 0
cur = 0
while True:
    o = rams[cur]//100
    x = (rams[cur]//10)%10
    y = rams[cur]%10
    count += 1
    if o == 1:
        print(count)
        break
    elif o == 2:
        registers[x] = y
    elif o == 3:
        registers[x] += y
        registers[x] %= 1000
    elif o == 4:
        registers[x] *= y
        registers[x] %= 1000
    elif o == 5:
        registers[x] = registers[y]
    elif o == 6:
        registers[x] += registers[y]
        registers[x] %= 1000
    elif o == 7:
        registers[x] *= registers[y]
        registers[x] %= 1000
    elif o == 8:
        registers[x] = rams[registers[y]]
    elif o == 9:
        rams[registers[y]] = registers[x]
    elif o == 0:
        if registers[y] != 0:
            cur = registers[x]
            continue
    cur += 1
