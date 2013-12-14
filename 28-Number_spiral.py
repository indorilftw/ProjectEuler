a = []
for i in xrange(1001):
  t = []
  for j in xrange(1001):
    t.append(0)
  a.append(t)
a[500][500] = 1
i = 500
j = 501
num = 2
a[i][j] = num
while num < 1001*1001:
  while (a[i][j-1] != 0):    # moving down
    num += 1
    i += 1
    a[i][j] = num
  while (a[i-1][j] != 0):    # moving left
    num += 1
    j -= 1
    a[i][j] = num
  while (a[i][j+1] != 0):    # moving up
    num += 1
    i -= 1
    a[i][j] = num
  while (a[i+1][j] != 0 and num < 1001*1001):    # moving right
    num += 1
    j += 1
    a[i][j] = num

total = 0
for i in xrange(1001):
  total += a[i][i]
  total += a[i][1000-i]
print total - 1