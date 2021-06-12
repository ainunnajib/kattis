a, b, k = map(int, input().split())
count = 0
for n in range(a, b+1):
    palindrome = True
    for base in range(2, min(k, n)+1):
        l = []
        x = n
        while x > 0:
            l.append(x%base)
            x //= base
        if l != l[::-1]:
            palindrome = False
            break
    if palindrome:
        count += 1
print(count)
