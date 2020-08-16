n = int(input())
for i in range(n):
    total = 0
    s = input()
    s = s[::-1]
    l = len(s)
    for j in range(int((l+1)/2)):
        total += int(s[2*j])
        if 2*j+1<l:
            x = int(s[2*j+1])
            x *= 2
            if x>9:
                x = x%9
                if x == 0:
                    x = 9
            total += x
    if total%10 == 0:
        print('PASS')
    else:
        print('FAIL')