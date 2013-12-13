from fractions import gcd
nom = denom = 1
for i in xrange(10,100):
  for j in xrange(10,i):
    if i % 10 == j / 10 and i / 10 != 0:
      n1 = i / 10
      n2 = j % 10
    elif i / 10 == j % 10 and i % 10 != 0:
      n1 = i % 10
      n2 = j / 10
    else:
      n1 = n2 = 1
    if j * 1.0 / i == n2 * 1.0 / n1:
      nom *= j
      denom *= i
print denom / gcd(nom, denom)