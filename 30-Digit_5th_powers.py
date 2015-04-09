total = 0
for i in xrange(10, 354295):
    sumPow = 0
    num = i
    while num > 0:
        (num, d) = divmod(num, 10)
        sumPow += d ** 5
    if sumPow == i:
        total += i
print total
