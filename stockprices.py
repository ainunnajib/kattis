import heapq
t = int(input())
for _ in range(t):
    n = int(input())
    ask, bid, price = 0, 0, 0
    buy = []
    heapq.heapify(buy)
    sell = []
    heapq.heapify(sell)
    for __ in range(n):
        s = input().split()
        x = int(s[1])
        p = int(s[-1])
        if s[0] == 'buy':
            for ___ in range(x):
                heapq.heappush(buy, -1*p)
        elif s[0] == 'sell':
            for ___ in range(x):
                heapq.heappush(sell, p)

        while len(buy) > 0 and len(sell) > 0:
            if buy[0] + sell[0] <= 0:
                heapq.heappop(buy)
                price = heapq.heappop(sell)
            else:
                break

        if len(buy) > 0:
            bid = -1*buy[0]
        else:
            bid = 0
        if len(sell) > 0:
            ask = sell[0]
        else:
            ask = 0

        print(ask if ask > 0 else '-', bid if bid > 0 else '-', price if price > 0 else '-')
