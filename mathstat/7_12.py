import numpy as np
from scipy.stats import binom, poisson, geom, laplace, pareto
from scipy.optimize import minimize
from scipy.special import gamma, digamma

# 1. Биномиальное распределение
sample1 = np.array([6, 5, 9, 5, 8, 7, 9, 6, 6, 7])
n1 = 10
p1 = np.mean(sample1)/n1

# 2. Распределение Пуассона
sample2 = np.array([5, 3, 3, 3, 5, 5, 1, 2, 3, 0])
a2 = np.mean(sample2)

# 3. Геометрическое распределение
sample3 = np.array([1, 2, 0, 4, 1, 4, 4, 1, 2, 2])
q3 = 1/(1 + np.mean(sample3))

# 4. Гипергеометрическое распределение (упрощенная оценка)
sample4 = np.array([6, 3, 7, 6, 4, 4, 5, 5, 6, 8])
m4 = 10
mean4 = np.mean(sample4)
# Оценка параметров через метод моментов
N_est = 42  # Общее количество элементов
nA4 = int(mean4 * N_est / m4)
nB4 = N_est - nA4

# 5. Распределение кратности звезд
sample5 = np.array([1, 2, 1, 3, 2, 1, 1, 2, 1, 2])
def neg_log_likelihood5(q):
    k = sample5
    return -np.sum(np.log((1-q)**2 * k * q**(k-1)))
res5 = minimize(neg_log_likelihood5, x0=0.5, bounds=[(0.01, 0.99)])
q5 = res5.x[0]

# 6. Равномерное распределение
sample6 = np.array([0.35, 1.83, 0.14, 0.64, 2.08, -0.46, 2.0, -0.31, -0.30, 1.87])
a6 = np.min(sample6)
b6 = np.max(sample6)

# 7. Показательное распределение
sample7 = np.array([0.61, 0.71, 1.27, 0.10, 1.49, 1.14, 2.15, 0.06, 0.74, 0.28])
lambda7 = 1/np.mean(sample7)

# 8. Гамма-распределение
sample8 = np.array([1.12, 4.34, 1.54, 3.11, 0.64, 0.62, 2.01, 2.13, 0.87, 0.79])
def neg_log_likelihood8(t):
    x = sample8
    return -np.sum((t-1)*np.log(x) - x - np.log(gamma(t)))
res8 = minimize(neg_log_likelihood8, x0=1.0, bounds=[(0.1, 10)])
t8 = res8.x[0]

# 9. Распределение Лапласа
sample9 = np.array([0.17, -0.22, -0.017, -0.16, 1.20, 0.057, -0.19, 0.19, 0.25, -0.32])
lambda9 = len(sample9)/np.sum(np.abs(sample9))

# 10. Распределение Парето
sample10 = np.array([1.63, 1.35, 1.80, 1.51, 1.56, 2.10, 1.36, 1.48, 1.24, 1.39])
a10 = np.min(sample10)
def neg_log_likelihood10(alpha):
    x = sample10
    return -np.sum(np.log(alpha/a10 * (a10/x)**(alpha+1)))
res10 = minimize(neg_log_likelihood10, x0=3.0, bounds=[(0.1, 10)])
alpha10 = res10.x[0]

# Вывод результатов
results = {
    1: {'p': p1},
    2: {'a': a2},
    3: {'q': q3},
    4: {'n_a': nA4, 'n_b': nB4},
    5: {'q': q5},
    6: {'a': a6, 'b': b6},
    7: {'lambda': lambda7},
    8: {'t': t8},
    9: {'lambda': lambda9},
    10: {'a': a10, 'alpha': alpha10}
}

for dist_num, params in results.items():
    print(f"Распределение {dist_num}:")
    for param, value in params.items():
        print(f"  {param} = {value:.3f}" if isinstance(value, float) else f"  {param} = {value}")
    print()