def recurring_cycle(d):
  for t in range(1, d):
    if 1 == 10**t % d:
      return t
  return 0

m = 0
for i in range(2,1001):
  curr = recurring_cycle(i)
  if curr > m:
    m = curr
    mpos = i
print mpos