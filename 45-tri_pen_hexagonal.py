triangle = set()
pentagonal = set()
hexagonal = set()
for i in xrange(100000):
    triangle.add(i * (i + 1) / 2)
    pentagonal.add(i * (3 * i - 1) / 2)
    hexagonal.add(i * (2 * i - 1))
result = hexagonal & pentagonal & triangle
print list(result)[3]
