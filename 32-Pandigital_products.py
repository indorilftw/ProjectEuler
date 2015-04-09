pand = set()
for i in xrange(1, 5000):
    for j in xrange(1, 100):
        s = sorted(str(i) + str(j) + str(i * j))
        if len(s) == 9 and "".join(s) == '123456789':
            pand.add(i * j)
print sum(pand)
