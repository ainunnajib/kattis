r, c = map(int, input().split())
a = max(list(map(int, input().split())))
b = max(list(map(int, input().split())))
print('possible' if a == b else 'impossible')