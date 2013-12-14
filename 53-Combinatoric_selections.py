from math import factorial

fact = {}
for i in xrange(101):
  fact[i] = factorial(i)

count = 0
for i in xrange(23,101):
  for j in xrange(i):
    if fact[i] / (fact[j] * fact[i-j]) > 1000000:
      count += 1
print count