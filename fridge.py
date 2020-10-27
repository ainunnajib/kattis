s = list(input())
s.sort()

l = [0 for _ in range(10)]
for c in s:
    l[int(c)] += 1

minl = min(l)
for i in range(10):
    if l[i] == minl:
        if i == 0:
            done = False
            for j in range(1, 10):
                if l[j] == minl:
                    print((minl+1) * str(j))
                    done = True
                    break
            if done:
                break

            print('1' + (minl+1) * '0')
        else:
            print((minl+1) * str(i))
        break
