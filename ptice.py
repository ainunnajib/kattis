#Adrian claims that the best sequence is: A, B, C, A, B, C, A, B, C, A, B, C ...
#Bruno is convinced that this is better: B, A, B, C, B, A, B, C, B, A, B, C ...
#Goran laughs at them and will use this sequence: C, C, A, A, B, B, C, C, A, A, B, B ...

n = int(input())
s = input()
adrian = "ABCABCABCABC"
bruno = "BABCBABCBABC"
goran = "CCAABBCCAABB"
a = 0
b = 0
g = 0
for i in range(n):
    if s[i] == adrian[i%12]:
        a += 1
    if s[i] == bruno[i%12]:
        b += 1
    if s[i] == goran[i%12]:
        g += 1
print(int(max(a,b,g)))
if a == max(a,b,g):
    print("Adrian")
if b == max(a,b,g):
    print("Bruno")
if g == max(a,b,g):
    print("Goran")