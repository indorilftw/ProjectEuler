s = "."
i = 1
while len(s) < 1000001:
  s = s + str(i)
  i += 1
ans = int(s[1]) * int(s[10]) * int(s[100]) * int(s[1000]) * int(s[10000]) * int(s[100000]) * int(s[1000000])
print ans