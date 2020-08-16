s = input().split()
code = s[0]
s = s[1]
result = ""
if code == 'E':
    curr = s[0]
    count = 0
    for i in range(len(s)):
        if s[i] == curr:
            count += 1
        else:
            result += curr + str(count)
            count = 1
            curr = s[i]
    result += curr + str(count)
elif code == 'D':
    for i in range(int(len(s)/2)):
        c = s[2*i]
        for j in range(int(s[2*i+1])):
            result += c
print(result)