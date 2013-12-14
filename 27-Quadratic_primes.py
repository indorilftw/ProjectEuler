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

primes = primegen(1000000)
longest = 0
for a in xrange(-1000, 1000):
  for b in xrange(-1000, 1000):
    count = 0
    for n in xrange(2000):
      if (n * n + a * n + b) in primes:
        count += 1
      else:
        break
    if count > longest:
      longest = count
      (maxA, maxB) = (a,b)
#print "a = {} , b = {} , max length = {}".format(maxA, maxB, longest) 
print "Answer = {}".format(maxA * maxB)