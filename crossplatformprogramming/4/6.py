A = [[1, 2, 3, 4], [5, 6, 7, 8]]
print('Mass A: ')
for i in A:
    print(' '.join(list(map(str, i))))
S = 0
for i in range(len(A)):
    for j in range(len(A[i])):
        S += A[i][j]
print('1 Example. Sum of elems: ', S)
S = 0
for row in A:
    for elem in row:
        S += elem
print('2 Example. Sem elems: ', S)