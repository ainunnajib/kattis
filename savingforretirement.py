import math
b, bret, bsav, a, asav = map(int, input().split())
print(math.ceil(((bret-b)*bsav+1)/asav)+a)
