import numpy


def primegen(n):
    mySieve = numpy.ones(n / 3 + (n % 6 == 2), dtype=numpy.bool)
    for i in xrange(1, int(n ** 0.5) / 3 + 1):
        if mySieve[i]:
            k = 3 * i + 1 | 1
            mySieve[k * k / 3::2 * k] = False
            mySieve[k * (k - 2 * (i & 1) + 4) / 3::2 * k] = False
    res = numpy.r_[2, 3, ((3 * numpy.nonzero(mySieve)[0][1:] + 1) | 1)]
    return [int(i) for i in res]

primes = primegen(1000000)
primeset = set(primes)
total = 0
for num in primes[4:]:
    temp = set()
    i = 1
    while 10 ** i < num:
        temp.add(num / (10 ** i))
        temp.add(num % (10 ** i))
        i += 1
    if temp.issubset(primeset):
        total += num
print total
