s = input()
aftervowel = False
result = ""
for c in s:
    if not aftervowel:
        result += c
    if c in "aiueo":
        aftervowel = not aftervowel
print(result)