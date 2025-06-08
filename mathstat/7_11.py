import numpy as np
from scipy.special import factorial
from scipy.optimize import fsolve
from scipy.special import gamma as gamma_func

def solve_moments():    
    # 7. Показательное распределение
    M1_7 = 0.69
    lambda7 = 1 / M1_7
    
    return {
        7: {'lambda': lambda7},
    }

results = solve_moments()
for dist_num, params in results.items():
    print(f"Распределение {dist_num}: {params}")