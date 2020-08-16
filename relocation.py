s = input().split()
n = int(s[0])
q = int(s[1])
s = input().split()
location = [-1]
for x in s:
    location.append(int(x))
for i in range(q):
    s = input().split()
    a = int(s[1])
    b = int(s[2])
    if s[0] == '1':
        location[a] = b
    elif s[0] == '2':
        if location[a] > location[b]:
            print(location[a] - location[b])
        else:
            print(location[b] - location[a])