import numpy as np
from scipy.stats import binom, poisson, geom, laplace, pareto
from scipy.optimize import minimize
from scipy.special import gamma, digamma

# 7. Показательное распределение
sample7 = np.array([0.61, 0.71, 1.27, 0.10, 1.49, 1.14, 2.15, 0.06, 0.74, 0.28])
lambda7 = 1/np.mean(sample7)

# Вывод результатов
results = {
    7: {'lambda': lambda7},
}

for dist_num, params in results.items():
    print(f"Распределение {dist_num}:")
    for param, value in params.items():
        print(f"  {param} = {value:.3f}" if isinstance(value, float) else f"  {param} = {value}")
    print()