s = input()
prev = ''
result = ""
for c in s:
    if c == prev:
        continue
    result += c
    prev = c
print(result)