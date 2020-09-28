r, s = map(int, input().split())
b = []
for _ in range(r):
    l = input()
    b.append([x == 'o' for x in l])

total = 0
maxmirko = 0
for i in range(r):
    for j in range(s):
        shake = 0
        if i > 0:
            if j > 0:
                shake += b[i-1][j-1]
            shake += b[i-1][j]
            if j < s-1:
                shake += b[i-1][j+1]
        if j > 0:
            shake += b[i][j-1]
        if j < s-1:
            shake += b[i][j+1]
        if i < r-1:
            if j > 0:
                shake += b[i+1][j-1]
            shake += b[i+1][j]
            if j < s-1:
                shake += b[i+1][j+1]

        if b[i][j]:
            total += shake
        else:
            maxmirko = max(maxmirko, shake)
total //= 2
total += maxmirko
print(total)
