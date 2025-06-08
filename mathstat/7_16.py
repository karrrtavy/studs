import numpy as np
from scipy.stats import norm, chi2, gamma

def calculate_confidence_intervals():
    results = {}
    
    # Задачи 1-4: Нормальное распределение, оценка параметра a
    # 1. n=10, sum_x=2.35, p=0.95
    n1, sum_x1, p1 = 10, 2.35, 0.95
    x_bar1 = sum_x1 / n1
    z_crit1 = norm.ppf(1 - (1 - p1)/2)
    margin1 = z_crit1 / np.sqrt(n1)
    results[1] = f"a ∈ ({x_bar1 - margin1:.5f}, {x_bar1 + margin1:.5f})_{p1} или a = {x_bar1:.3f} ± {margin1:.5f}_{p1}"
    
    # 2. n=20, sum_x=4.84, p=0.95
    n2, sum_x2, p2 = 20, 4.84, 0.95
    x_bar2 = sum_x2 / n2
    z_crit2 = norm.ppf(1 - (1 - p2)/2)
    margin2 = z_crit2 / np.sqrt(n2)
    results[2] = f"a ∈ ({x_bar2 - margin2:.5f}, {x_bar2 + margin2:.5f})_{p2} или a = {x_bar2:.3f} ± {margin2:.5f}_{p2}"
    
    # 3. n=14, sum_x=3.27, p=0.98
    n3, sum_x3, p3 = 14, 3.27, 0.98
    x_bar3 = sum_x3 / n3
    z_crit3 = norm.ppf(1 - (1 - p3)/2)
    margin3 = z_crit3 / np.sqrt(n3)
    results[3] = f"a ∈ ({x_bar3 - margin3:.5f}, {x_bar3 + margin3:.5f})_{p3} или a = {x_bar3:.5f} ± {margin3:.5f}_{p3}"
    
    # 4. n=13, sum_x=-1.71, p=0.98
    n4, sum_x4, p4 = 13, -1.71, 0.98
    x_bar4 = sum_x4 / n4
    z_crit4 = norm.ppf(1 - (1 - p4)/2)
    margin4 = z_crit4 / np.sqrt(n4)
    results[4] = f"a ∈ ({x_bar4 - margin4:.5f}, {x_bar4 + margin4:.5f})_{p4} или a = {x_bar4:.5f} ± {margin4:.5f}_{p4}"
    
    # Задачи 5-8: Нормальное распределение, оценка параметра σ²
    # 5. n=12, sum_x²=1.3, p=0.98
    n5, sum_x_sq5, p5 = 12, 1.3, 0.98
    chi2_low5 = chi2.ppf((1 - p5)/2, n5)
    chi2_high5 = chi2.ppf(1 - (1 - p5)/2, n5)
    sigma2_low5 = sum_x_sq5 / chi2_high5
    sigma2_high5 = sum_x_sq5 / chi2_low5
    results[5] = f"σ² ∈ ({sigma2_low5:.5f}, {sigma2_high5:.5f})_{p5}"
    
    # 6. n=29, sum_x²=1.2, p=0.96
    n6, sum_x_sq6, p6 = 29, 1.2, 0.96
    chi2_low6 = chi2.ppf((1 - p6)/2, n6)
    chi2_high6 = chi2.ppf(1 - (1 - p6)/2, n6)
    sigma2_low6 = sum_x_sq6 / chi2_high6
    sigma2_high6 = sum_x_sq6 / chi2_low6
    results[6] = f"σ² ∈ ({sigma2_low6:.5f}, {sigma2_high6:.5f})_{p6}"
    
    # 7. n=32, sum_x²=3.17, p=0.96
    n7, sum_x_sq7, p7 = 32, 3.17, 0.96
    chi2_low7 = chi2.ppf((1 - p7)/2, n7)
    chi2_high7 = chi2.ppf(1 - (1 - p7)/2, n7)
    sigma2_low7 = sum_x_sq7 / chi2_high7
    sigma2_high7 = sum_x_sq7 / chi2_low7
    results[7] = f"σ² ∈ ({sigma2_low7:.5f}, {sigma2_high7:.5f})_{p7}"
    
    # 8. n=50, sum_x²=5.34, p=0.98
    n8, sum_x_sq8, p8 = 50, 5.34, 0.98
    chi2_low8 = chi2.ppf((1 - p8)/2, n8)
    chi2_high8 = chi2.ppf(1 - (1 - p8)/2, n8)
    sigma2_low8 = sum_x_sq8 / chi2_high8
    sigma2_high8 = sum_x_sq8 / chi2_low8
    results[8] = f"σ² ∈ ({sigma2_low8:.5f}, {sigma2_high8:.5f})_{p8}"
    
    # Задачи 9-10: Показательное распределение, оценка параметра λ
    # 9. n=10, sum_x=2.35, p=0.96
    n9, sum_x9, p9 = 10, 2.35, 0.96
    gamma_low9 = gamma.ppf((1 - p9)/2, n9)
    gamma_high9 = gamma.ppf(1 - (1 - p9)/2, n9)
    lambda_low9 = gamma_low9 / sum_x9
    lambda_high9 = gamma_high9 / sum_x9
    results[9] = f"λ ∈ ({lambda_low9:.5f}, {lambda_high9:.5f})_{p9}"
    
    # 10. n=40, sum_x=15.33, p=0.98
    n10, sum_x10, p10 = 40, 15.33, 0.98
    gamma_low10 = gamma.ppf((1 - p10)/2, n10)
    gamma_high10 = gamma.ppf(1 - (1 - p10)/2, n10)
    lambda_low10 = gamma_low10 / sum_x10
    lambda_high10 = gamma_high10 / sum_x10
    results[10] = f"λ ∈ ({lambda_low10:.5f}, {lambda_high10:.5f})_{p10}"
    
    return results

results = calculate_confidence_intervals()

for problem, solution in results.items():
    print(f"Задача {problem}: {solution}")