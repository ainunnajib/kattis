s = input().split()
n = len(s)
count = 0
for w in s:
    if 'ae' in w:
        count += 1
if 4 * n <= 10 * count:
    print('dae ae ju traeligt va')
else:
    print('haer talar vi rikssvenska')
