count = 0
for num in range(1, 10001):
    lych = num + int(str(num)[::-1])
    for i in range(50):
        temp = str(lych)[::-1]
        if str(lych) == temp:
            count += 1
            break
        lych += int(temp)
print (10000 - count)
