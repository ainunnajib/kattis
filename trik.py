l = input()
cups = [1, 0, 0]
for c in l:
    if c == 'A':
        x = cups[0]
        cups[0] = cups[1]
        cups[1] = x
    elif c == 'B':
        x = cups[1]
        cups[1] = cups[2]
        cups[2] = x
    elif c == 'C':
        x = cups[0]
        cups[0] = cups[2]
        cups[2] = x
result = 1
for i in range(3):
    result += i*cups[i]
print(result)