t = int(input())
for _ in range(t):
    input()
    ncs, ne = map(int, input().split())
    iqcs = list(map(int, input().split()))
    iqe = list(map(int, input().split()))
    sumiqcs = sum(iqcs)
    sumiqe = sum(iqe)
    print(sum([1 if iq*ne > sumiqe and iq*ncs < sumiqcs else 0 for iq in iqcs]))
