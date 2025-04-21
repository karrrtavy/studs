a = [0, 1, 2, 4, 10, 13, 21, 34, 55, 89, 100, 16]
for elem in a:
    if elem < 35 and elem % 2 == 0:
        print(elem)

print("Длина массива: ", len(a))
sum = float(0)
for elem in a:
    sum += elem
print("Среднее арифметическое: ", sum // len(a))
print("Max: ", max(a), "Min: ", min(a))

# или
print("_____")
N = int(input("Размер массива = "))
S = 0
array = []

for i in range(N):
    a1 = int(input("Введите число: "))
    array.append(a1)
    S = S + a1
    C = S / N
print("Среднее арифметическое: ", C)
print(f"Max: {max(array)}, Min: {min(array)}")

