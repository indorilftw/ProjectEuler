total = 0
for n in xrange(1000000):
    if str(n) == str(n)[::-1]:
        b = bin(n)[2:]
        if b == b[::-1]:
            total += n
print total
