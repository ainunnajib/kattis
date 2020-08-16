n = int(input())
a = 'abcdefghijklmnopqrstuvwxyz'
for i in range(n):
    s = input().lower()
    r = ""
    for c in a:
        if c not in s:
            r += c
    if r == "":
        print("pangram")
    else:
        print("missing " + r)