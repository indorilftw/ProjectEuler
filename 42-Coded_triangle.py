triangles = []
for i in xrange(35):
  triangles.append(i * (i + 1) / 2)
with open('files/42-words.txt', 'r') as myFile:
  s = myFile.read()
words = [string[1:-1] for string in s.split(',')]
count = 0
for word in words:
  subtotal = 0
  for let in word:
    subtotal += ord(let) - 64
  if subtotal in triangles:
    count += 1
print count