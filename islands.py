p = int(input())
for _ in range(1, p+1):
    l = list(map(int, input().split()))
    case = l[0]
    l = l[1:]
    count = 0
    for i in range(1, 11):
        for j in range(i+1, 12):
            x = min(l[i:j])
            if x > l[i-1] and x > l[j]:
                count += 1
    print(case, count)
