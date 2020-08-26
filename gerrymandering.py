p, d = map(int, input().split())
votesa = {}
votesb = {}
totalvotes = 0
for i in range(1, d+1):
    votesa[i] = 0
    votesb[i] = 0
for _ in range(p):
    di, va, vb = map(int, input().split())
    votesa[di] += va
    votesb[di] += vb
    totalvotes += va + vb

totalwasteda = 0
totalwastedb = 0
for i in range(1, d+1):
    if votesa[i] > votesb[i]:
        win = 'A'
        wasteda = votesa[i] - ((votesa[i] + votesb[i])//2 + 1)
        wastedb = votesb[i]
    else:
        win = 'B'
        wasteda = votesa[i]
        wastedb = votesb[i] - ((votesa[i] + votesb[i])//2 + 1)
    print(win, wasteda, wastedb)
    totalwasteda += wasteda
    totalwastedb += wastedb
print(abs(totalwasteda - totalwastedb)/totalvotes)
