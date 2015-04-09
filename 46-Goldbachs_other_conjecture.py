import numpy


class LoopBreakException(Exception):
    pass


def primegen(n):
    mySieve = numpy.ones(n / 3 + (n % 6 == 2), dtype=numpy.bool)
    for i in xrange(1, int(n ** 0.5) / 3 + 1):
        if mySieve[i]:
            k = 3 * i + 1 | 1
            mySieve[k * k / 3::2 * k] = False
            mySieve[k * (k - 2 * (i & 1) + 4) / 3::2 * k] = False
    res = numpy.r_[2, 3, ((3 * numpy.nonzero(mySieve)[0][1:] + 1) | 1)]
    return [int(i) for i in res]


def main():
    primes = primegen(10000)
    pr_set = frozenset(primes)
    dbl_squares = [2 * x * x for x in xrange(1, 100)]
    num = 3
    for _ in xrange(20000):
        if num not in pr_set:
            try:
                found = False
                for i in primes:
                    for j in dbl_squares:
                        if i > num:
                            raise LoopBreakException
                        elif j > num:
                            break
                        elif num == i + j:
                            found = True
                            raise LoopBreakException
            except LoopBreakException:
                if not found:
                    print num
                    return
        num += 2
    else:
        print("Not found, increase number of iterations")


if __name__ == '__main__':
    main()
