def print_matrix(mat):
    for row in mat:
        print(' '.join(map(str, row)))
N = int(input("reg num: "))
if N % 2 == 0:
    print("not reg num")
    exit()
print("input elems: ")
matrix = [list(map(int, input().split())) for _ in range(N)]
center = N // 2
max_elem = float("-inf")
max_pos = None
for i in range(N):
    if matrix[i][i] > max_elem:
        max_elem = matrix[i][i]
        max_pos = (i, i)
    if matrix[i][N - 1 - i] > max_elem:
        max_elem = matrix[i][N - 1 - i]
        max_pos = (i, N - 1 - i)
print("\max elem on diag: ")
print("elem in centre:", matrix[center][center])
matrix[center][center], matrix[max_pos[0]][max_pos[1]] = matrix[max_pos[0]][max_pos[1]], matrix[center][center]
print("\nafter: ")
print_matrix(matrix)