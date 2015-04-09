with open('files/22names.txt', 'r') as myFile:
    s = myFile.read()
names = [string[1:-1] for string in s.split(',')]
names.sort()
total = 0
for idx, name in enumerate(names):
    subtotal = 0
    for let in name:
        subtotal += ord(let) - 64
    total += subtotal * (idx + 1)
print total
