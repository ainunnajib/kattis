a = [".#...#...*..",
     "#.#.#.#.*.*.",
     ". .#. .*. .*",
     "#.#.#.#.*.*.",
     ".#...#...*.."]
l = [".", ".", "#", ".", "."]
s = input()
for i in range(5):
    row = l[i]
    if i == 2:
        for k in range(len(s)):
            row += '.' + s[k] + '.'
            if k%3 == 0 or (len(s)%3 == 2 and k == len(s)-1):
                row += '#'
            else:
                row += '*'
    else:
        for j in range(len(s)//3):
                row += a[i]
    if i != 2:
        row += a[i][:(len(s)%3)*4]
    print(row)
