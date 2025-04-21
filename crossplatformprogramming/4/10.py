n = 3
a = []
for i in range(n):
    b = []
    for j in range(n):
        print(f'Input [{i, j}]')
        b.append(int(input()))
    a.append(b)
for i in range(n):
    for j in range(n):
        print(a[i][j], end=' ')
    print()
maximum = a[0][2]
for i in range(n):
    for j in range(n):
        if maximum < a[i][2]:
            maximum = [i][2]
print('Max in 3 col: ', maximum)
maximum = a[1][0]
for i in range(n):
    for j in range(n):
        if maximum < a[1][j]:
            maximum = a[1][j]
print('Max in 2 row: ', maximum)