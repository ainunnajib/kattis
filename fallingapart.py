n = int(input())
s = list(map(int, input().split()))
s.sort(reverse = True)
a = sum(s[::2])
b = sum(s[1::2])
print(a, b)