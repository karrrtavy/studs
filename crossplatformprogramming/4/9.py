n = 3
A = []
for i in range(n):
    A.append([9] * n)
for i in range(n):
    for j in range(n):
        print(A[i][j], end=' ')
    print()
for i in range(n):
    A[i] = [2] * i + [0] + [1] * (n - i -1)
print()
for i in range(n):
    for j in range(n):
        print(A[i][j], end=' ')
    print()