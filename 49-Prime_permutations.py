import numpy
from itertools import permutations


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
    pr = [i for i in primegen(10000) if i > 1000]
    pset = set(pr)
    lst = []
    for i in pr:
        for num in permutations(str(i)):
            k = int("".join(num))
            if k == i:
                continue
            if k in pset and (2 * k - i) in pset and sorted(str(2 * k - i)) == sorted(str(i)):
                s = str(i) + str(k) + str(2 * k - i)
                lst.append(s)
                if len(lst) > 1:
                    print s
                    return 0

if __name__ == '__main__':
    main()
