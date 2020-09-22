case = 0
while True:
    try:
        case += 1

        n = int(input())
        l = []
        for _ in range(n):
            l.append(int(input()))
        s = []
        for i in range(n):
            for j in range(i+1, n):
                s.append(l[i] + l[j])
        s.sort()
        ls = len(s)

        m = int(input())
        print('Case', str(case)+':')
        for _ in range(m):
            q = int(input())
            i = 0
            while i < ls:
                if q < s[i]:
                    break
                i += 1
            if i == 0:
                ans = s[0]
            elif i == ls:
                ans = s[-1]
            else:
                if s[i] - q >= q - s[i-1]:
                    ans = s[i-1]
                else:
                    ans = s[i]

            print('Closest sum to', q, 'is', str(ans) + '.')

    except EOFError:
        break
