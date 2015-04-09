coins = [1, 2, 5, 10, 20, 50, 100, 200]
totalSum = 200
coinCount = {}
for y in xrange(0, totalSum + 1):
    coinCount[y, 0] = 1
for y in xrange(0, totalSum + 1):
    # print y, ":", 1,
    for x in xrange(1, len(coins)):
        coinCount[y, x] = 0
        if y >= coins[x]:
            coinCount[y, x] += coinCount[y, x - 1]
            coinCount[y, x] += coinCount[y - coins[x], x]
        else:
            coinCount[y, x] = coinCount[y, x - 1]
        # print coinCount[y, x],
    # print
print coinCount[y, x]
