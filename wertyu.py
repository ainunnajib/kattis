key = [ "`1234567890-=", "QWERTYUIOP[]\\", "ASDFGHJKL;'", "ZXCVBNM,./" ]
while True:
    try:
        s = input()
        result = ""
        for c in s:
            if c == ' ':
                result += c
                continue
            for row in key:
                if c in row:
                    result += row[row.index(c)-1]
                    break
        print(result)
    except EOFError:
        break