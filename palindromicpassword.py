palindromes = set()
for i in range(100, 1000):
    s = str(i)
    s += s[::-1]
    palindromes.add(s)

n = int(input())
for _ in range(n):
    x = int(input())
    i = 0
    while True:
        if str(x-i) in palindromes:
            print(str(x-i))
            break
        if str(x+i) in palindromes:
            print(str(x+i))
            break
        i += 1
