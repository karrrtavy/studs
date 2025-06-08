import numpy as np
from scipy.stats import t, chi2

def calculate_confidence_intervals(n, M_star, D_star, p_a, p_sigma2):
    # Доверительный интервал для математического ожидания (a)
    alpha_a = 1 - p_a
    t_critical = t.ppf(1 - alpha_a / 2, df=n-1)
    se = np.sqrt(D_star / n)  # стандартная ошибка среднего
    margin_a = t_critical * se
    a_lower = M_star - margin_a
    a_upper = M_star + margin_a
    
    # Доверительный интервал для дисперсии (σ²)
    alpha_sigma2 = 1 - p_sigma2
    chi2_lower = chi2.ppf(1 - alpha_sigma2 / 2, df=n-1)
    chi2_upper = chi2.ppf(alpha_sigma2 / 2, df=n-1)
    sigma2_lower = (n - 1) * D_star / chi2_lower
    sigma2_upper = (n - 1) * D_star / chi2_upper
    
    return {
        'a': (a_lower, a_upper),
        'sigma2': (sigma2_lower, sigma2_upper),
        'margin_a': margin_a
    }

# Примеры данных
data = [
    {"n": 19, "M_star": 1.2, "D_star": 1.3, "p_a": 0.99, "p_sigma2": 0.98},
    {"n": 13, "M_star": -0.5, "D_star": 2.7, "p_a": 0.98, "p_sigma2": 0.96},
    {"n": 20, "M_star": 2.3, "D_star": 3.2, "p_a": 0.99, "p_sigma2": 0.98},
    {"n": 28, "M_star": 3.1, "D_star": 1.2, "p_a": 0.98, "p_sigma2": 0.90},
    {"n": 25, "M_star": 0.5, "D_star": 1.9, "p_a": 0.98, "p_sigma2": 0.96},
    {"n": 50, "M_star": -0.7, "D_star": 0.2, "p_a": 0.99, "p_sigma2": 0.98},
    {"n": 100, "M_star": 1.3, "D_star": 0.8, "p_a": 0.98, "p_sigma2": 0.99},
    {"n": 200, "M_star": -1.2, "D_star": 0.7, "p_a": 0.99, "p_sigma2": 0.98},
    {"n": 170, "M_star": -3.2, "D_star": 1.4, "p_a": 0.99, "p_sigma2": 0.98},
    {"n": 90, "M_star": 12.3, "D_star": 1.1, "p_a": 0.98, "p_sigma2": 0.99}
]

# Вычисление и вывод результатов
for i, params in enumerate(data, start=1):
    result = calculate_confidence_intervals(**params)
    print(f"{i}. a ∈ ({result['a'][0]:.4f}, {result['a'][1]:.4f})_{params['p_a']} или a = {params['M_star']} ± {result['margin_a']:.4f}_{params['p_a']},")
    print(f"   σ² ∈ ({result['sigma2'][0]:.4f}, {result['sigma2'][1]:.4f})_{params['p_sigma2']}.\n")