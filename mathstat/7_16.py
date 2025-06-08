import numpy as np
from scipy.stats import norm, chi2, gamma

def calculate_confidence_intervals():
    results = {}
    
    # 7. n=32, sum_x²=3.17, p=0.96
    n7, sum_x_sq7, p7 = 32, 3.17, 0.96
    chi2_low7 = chi2.ppf((1 - p7)/2, n7)
    chi2_high7 = chi2.ppf(1 - (1 - p7)/2, n7)
    sigma2_low7 = sum_x_sq7 / chi2_high7
    sigma2_high7 = sum_x_sq7 / chi2_low7
    results[7] = f"σ² ∈ ({sigma2_low7:.5f}, {sigma2_high7:.5f})_{p7}"
        
    return results

results = calculate_confidence_intervals()

for problem, solution in results.items():
    print(f"Задача {problem}: {solution}")