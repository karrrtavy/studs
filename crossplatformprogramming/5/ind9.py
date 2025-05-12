import numpy as np

<<<<<<< HEAD
with open(r'crossplatformprogramming/5/besi.txt', 'r', encoding='utf-8') as f:
    data = f.read().strip()
=======
# Значения x от -6 до 6 с шагом 1
x = np.arange(-6, 7, 1)

# Вычисляем y1 и y2 по формулам
y1 = np.sqrt(1 + 2 * x**2 - np.sin(x)**2)
y2 = (2 + x) / (np.sqrt(2) + np.exp(x))
>>>>>>> refs/remotes/origin/main

# Сумма y
y = y1 + y2

# Сортировка y по возрастанию
y_sorted = np.sort(y)

<<<<<<< HEAD
with open(r'crossplatformprogramming/5/besi2.txt', 'w', encoding='utf-8') as file2:    
    for i in besi:
        file2.write(i)
        if  i[len(i) - 1] == '.' or i[len(i) - 1] == '?':
            count += 1
        if count == 16:
            break

count = 0

with open(r'crossplatformprogramming/5/reverseword.txt', 'w', encoding='unt-8'):
    for i in besi:
        if count % 2 != 0:
            
=======
# Нахождение минимумов
min_y1 = np.min(y1)
min_y2 = np.min(y2)

# Сравнение минимумов
if min_y1 < min_y2:
    compare = "min(y1) меньше min(y2)"
elif min_y1 > min_y2:
    compare = "min(y1) больше min(y2)"
else:
    compare = "min(y1) равно min(y2)"

# Вывод результатов
print("x:", x)
print("y1:", y1)
print("y2:", y2)
print("y = y1 + y2:", y)
print("y (sorted):", y_sorted)
print(f"min(y1) = {min_y1}")
print(f"min(y2) = {min_y2}")
print("Сравнение минимумов:", compare)
>>>>>>> refs/remotes/origin/main
