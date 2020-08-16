line = input().split()
inp = [ int(x) for x in line ]
correct = [1, 1, 2, 2, 2, 8]
result = [ correct[i] - inp[i] for i in range(6) ]
print(*result, sep = " ")