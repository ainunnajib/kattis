m = int(input())
while m != 0:
    w, h = map(int, input().split())
    cx, cy, maxx, maxy = 0, 0, 0, 0
    while w != -1 and h != -1:
        if cx + w > m:
            cy += maxy
            maxx = max(maxx, cx)
            cx = w
            maxy = h
        else:
            cx += w
            maxy = max(maxy, h)
        w, h = map(int, input().split())
    cy += maxy
    maxx = max(maxx, cx)
    print(f'{maxx} x {cy}')
    m = int(input())
