import math
while True:
    try:
        n = int(input())
        sumdiv = 1
        for i in range(2, math.floor(math.sqrt(n))+1):
            if n%i == 0:
                sumdiv += i
                if n//i != i:
                    sumdiv += n//i
                if sumdiv > n+2:
                    break
        if sumdiv == n:
            print(n, 'perfect')
        elif abs(n-sumdiv) <= 2:
            print(n, 'almost perfect')
        else:
            print(n, 'not perfect')
    except EOFError:
        break
