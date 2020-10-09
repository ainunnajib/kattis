n = int(input())
sum = n
while n != 1:
    if n % 2 == 0:
        n //= 2
    else:
        n = 3*n + 1
    sum += n
print(sum)
