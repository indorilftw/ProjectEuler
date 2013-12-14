def sumdiv(n):
  sum = 0
  for i in xrange(1, n//2 + 1):
    if n % i == 0:
      sum += i
  return sum

total = 0
for i in xrange(1,10001):
  temp = sumdiv(i)
  if temp < 10000 and temp > i and sumdiv(temp) == i:
    total += i + temp
print total