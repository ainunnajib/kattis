t = int(input())
for _ in range(t):
    input()
    n = int(input())
    sum = 0
    for __ in range(n):
        sum += int(input())
    print('YES' if sum%n == 0 else 'NO')
