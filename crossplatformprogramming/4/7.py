n = 3
A = []
for i in range(n):
    A.append([9] * n)
for i in range(n):
    for j in range(n):
        print(A[i][j], end=' ')
    print()
for i in range(n):
    for j in range(n):
        if i < j:
            A[i][j] = 1
        elif i > j:
            A[i][j] = 2
        else:
            A[i][j] = 0
print()
for i in range(n):
    for j in range(n):
        print(A[i][j], end=' ')
    print()