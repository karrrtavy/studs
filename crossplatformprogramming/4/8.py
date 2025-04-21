n = 3 
A = []
for i in range(n):
    A.append([9] * n)
for i in range(n):
    for j in range(n):
        print(A[i][j], end=' ')
    print()
for i in range(n):
    for j in range(0, i):
        A[i][j] = 2
    A[i][i] = 0
    for j in range(i + 1, n):
        A[i][j] = 1
print()
for i in range(n):
    for j in range(n):
        print(A[i][j], end=' ')
    print()