from math import factorial

total = 0
# apparently only 145 and 40585 are factorions
for num in xrange(3, 2000000):
    lst = [int(i) for i in str(num)]
    if sum(map(lambda x: factorial(x), lst)) == num:
        total += num
print total
