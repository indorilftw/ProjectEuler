a = [i * (3 * i - 1) / 2 for i in xrange(1, 100000)]
b = set(a)
d = 9999999999999
for idx, n1 in enumerate(a):
    for n2 in a[idx + 1:]:
        if n2 - n1 > d:
            break
        if (n1 + n2) in b and (n2 - n1) in b:
            print n1, n2
            d = n2 - n1
            break
print d
