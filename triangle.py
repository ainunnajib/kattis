import sys, math
case = 0
for n in sys.stdin.readlines():
    case += 1
    n = int(n)
    d = math.floor(math.log10(3)*(n+1) - math.log10(2)*n) + 1
    print('Case', str(case)+':', d)
