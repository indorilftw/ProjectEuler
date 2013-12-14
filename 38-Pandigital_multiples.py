pand = set()
for i in xrange(1,10000):
  s = str(i)
  j = 2
  while len(s) < 9:
    s += str(j * i)
    j += 1
  if len(s) == 9 and "".join(sorted(s)) == '123456789':
    pand.add(int(s))
print max(pand)