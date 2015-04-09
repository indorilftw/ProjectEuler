def sumdiv(n):
    sum = 0
    for i in xrange(1, n // 2 + 1):
        if n % i == 0:
            sum += i
    return sum

abundant = set()
numbers = set(range(20162))
abundantSums = set()
for i in xrange(12, 20162):
    temp = sumdiv(i)
    if temp > i:
        abundant.add(i)
        for j in abundant:
            k = i + j
            if k < 20162:
                abundantSums.add(k)
allInts = numbers - abundantSums
print sum(allInts)
