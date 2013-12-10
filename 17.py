with open('files/17text.txt', 'r') as myFile:
    s = myFile.read()
s2 = "".join(s.split())
print len(s2)