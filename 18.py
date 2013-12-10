rows = []
with open("files/18_path.txt", "r") as myFile:
  for line in myFile: 
    rows.append([int(i) for i in line.split(" ")])
 
a = []
for i in range(len(rows)-2, -1 , -1):
  for j in range(i + 1):
    a.append((i, j))
for i,j in a:
  rows[i][j] +=  max([rows[i+1][j],rows[i+1][j+1]])

print rows[0][0]