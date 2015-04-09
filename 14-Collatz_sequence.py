maxSeq = 1
maxNum = 1
for num in xrange(2, 1000000):
    temp = 0
    num2 = num
    while num2 > 1:
        temp += 1
        if (num2 % 2 == 0):
            num2 = num2 / 2
        else:
            num2 = 3 * num2 + 1
    if temp > maxSeq:
        maxSeq = temp
        maxNum = num
print maxNum, maxSeq
