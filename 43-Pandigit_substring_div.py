from itertools import permutations
perms = permutations('0123456789')
total = 0
for num in perms:
    if ((int(num[1] + num[2] + num[3]) % 2 == 0) and (int(num[2] + num[3] + num[4]) % 3 == 0) and
            (int(num[3] + num[4] + num[5]) % 5 == 0) and (int(num[4] + num[5] + num[6]) % 7 == 0) and
            (int(num[5] + num[6] + num[7]) % 11 == 0) and (int(num[6] + num[7] + num[8]) % 13 == 0) and
            (int(num[7] + num[8] + num[9]) % 17 == 0)):
        total += int("".join(num))
print total
