terms = []
for i in xrange(2, 101):
    for j in xrange(2, 101):
        k = i ** j
        if k not in terms:
            terms.append(k)
print len(terms)
