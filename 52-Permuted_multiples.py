i = 10
while True:
    i += 1
    if set(str(i)) == set(str(2 * i)) == set(str(3 * i)) == set(str(4 * i)) == set(str(5 * i)) == set(str(6 * i)):
        break
print i
