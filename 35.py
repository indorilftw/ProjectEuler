import numpy

def primegen(n):
  mySieve = numpy.ones(n / 3 + (n % 6 == 2), dtype=numpy.bool)
  for i in xrange(1, int(n**0.5)/3+1):
    if mySieve[i]:
      k = 3 * i + 1 | 1
      mySieve[k * k / 3::2 * k] = False
      mySieve[k * (k - 2 * (i & 1) + 4) / 3::2 * k] = False
  res = numpy.r_[2, 3, ((3 * numpy.nonzero(mySieve)[0][1:] + 1) | 1)]
  return set([int(i) for i in res])

primes = primegen(10000000)
count = 0
for i in primes:
  n1 = list(str(i))
  mySet = set()
  for j in xrange(len(n1)):
    n1.insert(0,n1.pop())
    mySet.add(int("".join(n1)))
  if mySet.issubset(primes):
    count += 1
print count