import numpy as np
x = np.arange(-6, 7, 1)
y1 = np.sqrt(1 + 2 * x**2 - np.sin(x)**2)
y2 = (2 + x) / (np.sqrt(2) + np.exp(x))
y = y1 + y2
y_sorted = np.sort(y)
min_y1 = np.min(y1)
min_y2 = np.min(y2)
if min_y1 < min_y2:
    compare = "min(y1) < min(y2)"
elif min_y1 > min_y2:
    compare = "min(y1) > min(y2)"
else:
    compare = "min(y1) = min(y2)"
print("x:", x)
print("y1:", y1)
print("y2:", y2)
print("y = y1 + y2:", y)
print("y (sorted):", y_sorted)
print(f"min(y1) = {min_y1}")
print(f"min(y2) = {min_y2}")
print("Сравнение минимумов:", compare)