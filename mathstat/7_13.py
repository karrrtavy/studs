import numpy as np
from scipy.optimize import curve_fit

# Экспоненциальная функция
def exponential(x, a1, a2):
    return a1 * np.exp(a2 * x)

# Данные для задачи 7
x_data = np.array([-1, -0.75, -0.5, -0.25, 0, 0.25, 0.5, 0.75, 1])
y_data = np.array([6.94, 4.65, 3.16, 2.30, 1.37, 0.74, 0.73, 0.25, 0.16])

# Начальное приближение
p0 = [1.5, -1.5]

# Аппроксимация
popt, pcov = curve_fit(exponential, x_data, y_data, p0=p0)
a1, a2 = popt

# Вывод результата
print(f"Задача 7:")
print(f"y = {a1:.4f} * exp({a2:.4f}x)")
