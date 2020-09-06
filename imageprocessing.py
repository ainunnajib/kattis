h, w, n, m = map(int, input().split())

image = []
for _ in range(h):
    image.append(list(map(int, input().split())))

kernel = []
for _ in range(n):
    kernel.append(list(map(int, input().split()))[::-1])
kernel = kernel[::-1]

r = [[0 for i in range(w-m+1)] for j in range(h-n+1)]
for j in range(h-n+1):
    for i in range(w-m+1):
        for y in range(n):
            for x in range(m):
                r[j][i] += image[j+y][i+x] * kernel[y][x]

for row in r:
    print(' '.join([str(x) for x in row]))
