import numpy
from itertools import permutations

def primegen(n):
  mySieve = numpy.ones(n / 3 + (n % 6 == 2), dtype=numpy.bool)
  for i in xrange(1, int(n**0.5)/3+1):
    if mySieve[i]:
      k = 3 * i + 1 | 1
      mySieve[k * k / 3::2 * k] = False
      mySieve[k * (k - 2 * (i & 1) + 4) / 3::2 * k] = False
  res = numpy.r_[2, 3, ((3 * numpy.nonzero(mySieve)[0][1:] + 1) | 1)]
  return set([int(i) for i in res])

pand = []
lst = []
s = ""
for i in xrange(1,10):
  s = s + str(i)
  pand.append(s)
primes = primegen(987654321)
for i in pand[::-1]:
  for j in permutations(i, len(i)):
    k = int("".join(j))
    if k in primes:
      lst.append(k)
  if lst:
    break
print max(lst)