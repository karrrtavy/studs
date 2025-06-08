import numpy as np
from scipy.optimize import curve_fit
import math

# Функции моделей
def linear(x, a1, a2):
    return a1 * x + a2

def quadratic(x, a1, a2, a3):
    return a1 * x**2 + a2 * x + a3

def exponential(x, a1, a2):
    return a1 * np.exp(a2 * x)

def tangent(x, a1, a2):
    return np.tan(a1 * x + a2)

# Данные для всех задач
x_data = np.array([-1, -0.75, -0.5, -0.25, 0, 0.25, 0.5, 0.75, 1])

y_data = {
    1: np.array([2.08, 1.83, 1.57, 1.13, 0.89, 0.75, 0.30, 0.06, -0.01]),
    2: np.array([1.09, 1.47, 1.95, 2.47, 2.98, 3.54, 4.20, 4.42, 4.89]),
    3: np.array([3.90, 3.71, 3.63, 3.22, 3.04, 2.71, 2.45, 2.25, 2.03]),
    4: np.array([-0.14, 1.08, 1.61, 2.34, 3.16, 3.41, 3.58, 3.96, 4.02]),
    5: np.array([2.98, 2.47, 2.13, 2.00, 1.95, 2.05, 2.31, 2.46, 3.08]),
    6: np.array([2.04, 0.92, -0.37, -0.86, -1.20, -1.17, -1.17, -0.69, -0.26]),
    7: np.array([6.94, 4.65, 3.16, 2.30, 1.37, 0.74, 0.73, 0.25, 0.16]),
    8: np.array([0.10, -0.08, -0.14, -0.83, -1.95, -5.53, -14.6, -40.3, -109]),
    9: np.array([2.57, 1.47, 1.12, 0.85, 0.57, 0.17, -0.03, -0.10, -0.34]),
    10: np.array([-0.62, -0.28, 0.05, 0.10, 0.26, 0.51, 0.94, 1.29, 2.22])
}

# Решение для каждой задачи
results = {}

# Линейные модели (задачи 1-3)
for i in range(1, 4):
    popt, pcov = curve_fit(linear, x_data, y_data[i])
    results[i] = {'a1': popt[0], 'a2': popt[1]}

# Квадратичные модели (задачи 4-6)
for i in range(4, 7):
    popt, pcov = curve_fit(quadratic, x_data, y_data[i])
    results[i] = {'a1': popt[0], 'a2': popt[1], 'a3': popt[2]}

# Экспоненциальные модели (задачи 7-8)
for i in range(7, 9):
    # Начальные приближения для лучшей сходимости
    if i == 7:
        p0 = [1.5, -1.5]
    else:
        p0 = [-2, 4]
    popt, pcov = curve_fit(exponential, x_data, y_data[i], p0=p0)
    results[i] = {'a1': popt[0], 'a2': popt[1]}

# Тангенс модели (задачи 9-10)
for i in range(9, 11):
    # Ограничиваем параметры для избежания сингулярностей
    popt, pcov = curve_fit(tangent, x_data, y_data[i], 
                          bounds=([-1, -math.pi/2], [1, math.pi/2]))
    results[i] = {'a1': popt[0], 'a2': popt[1]}

# Вывод результатов с округлением
for i in range(1, 11):
    print(f"Задача {i}:")
    if i <= 3:
        a1, a2 = results[i]['a1'], results[i]['a2']
        print(f"y = {a2:.4f} + {a1:.4f}x")
    elif i <= 6:
        a1, a2, a3 = results[i]['a1'], results[i]['a2'], results[i]['a3']
        print(f"y = {a1:.4f}x² + {a2:.4f}x + {a3:.4f}")
    elif i <= 8:
        a1, a2 = results[i]['a1'], results[i]['a2']
        print(f"y = {a1:.4f} exp({a2:.4f}x)")
    else:
        a1, a2 = results[i]['a1'], results[i]['a2']
        print(f"y = tan({a1:.5f}x + {a2:.5f})")
    print()