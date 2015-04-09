from math import sqrt
from collections import defaultdict

p = defaultdict(int)
for i in xrange(1, 500):
    for j in xrange(1, 500):
        k = sqrt(i * i + j * j)
        if k == int(k) and k < 1000:
            p[i + j + int(k)] += 1
print max(p, key=p.get)
