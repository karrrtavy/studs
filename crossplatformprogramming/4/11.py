m = int(input('Input rows: '))
n = int(input('Input columns: '))
a = []
for i in range(m):
    b = []
    for j in range(n):
        print(f'Input [{i, j}]')
        b.append(int(input()))
    a.append(b)
print('Ishdniy Mass: ')
for i in range(m):
    for j in range(n):
        print(a[i][j], end=' ')
    print()
for i in range(m):
    for j in range(n):
        if a[i][j] < 0: a[i][j] = 0
        elif a[i][j] > 0: a[i][j] = 1
print('Edited mass: ')
for i in range(m):
    for j in range(n):
        print(a[i][j], end=' ')
    print()