w, p = map(int, input().split())
l = [0]
l += list(map(int, input().split()))
l.append(w)
d = {}
for i in range(p+2):
    for j in range(i+1, p+2):
        d[l[j]-l[i]] = True
print(' '.join(list(map(str, sorted(d.keys())))))
