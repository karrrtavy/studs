from random import randint
a = []
n = int(input())
for i in range(n):
    row = []
    for j in range(n):
        row.append(randint(1, 9))
        print(row[j], end=' ')
    a.append(row)
    print()
max_in_rows = [max(row) for row in a]
print("max in rows: ", max_in_rows)
min_in_cols = [min(a[i][j] for i in range(n)) for j in range(n)]
print("min in cols: ", min_in_cols)
