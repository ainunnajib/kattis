n = int(input())
for i in range(n):
    l = input().split()
    set = int(l[0])
    base = int(l[1])
    number = int(l[2])
    total = 0
    while number > 0:
        digit = number%base
        total += digit*digit
        number = int((number - digit)/base)
    print(str(set) + " " + str(total))
