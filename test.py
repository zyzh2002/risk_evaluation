a = [[1,2,3],[4,5,6],[7,8,9]]

l = []
for i in range(len(a)):
    for j in range(len(a[i])):
        l.append(a[i][j])
print(l)

b = [[1,2,3],[4,4,4],[1,1,1]]

for i in range(len(a)):
    for j in range(len(a[i])):
        print(i*len(a)+j)
        b[i][j]=l[i*len(a)+j]

print(b)