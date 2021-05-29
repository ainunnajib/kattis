n = int(input())
if n % 2 == 1:
    print('still running')
else:
    t = 0
    for _ in range(n//2):
        t -= int(input())
        t += int(input())
    print(t)