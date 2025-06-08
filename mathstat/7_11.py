import numpy as np
from scipy.special import factorial
from scipy.optimize import fsolve
from scipy.special import gamma as gamma_func

def solve_moments():
    # 1. Биномиальное распределение
    n1 = 10
    M1_1 = 6.8
    p1 = M1_1 / n1
    
    # 2. Распределение Пуассона
    M1_2 = 3.24
    a2 = M1_2
    
    # 3. Геометрическое распределение
    M1_3 = 2.1
    q3 = M1_3 / (1 + M1_3)
    
    # 4. Гипергеометрическое распределение
    def equations4(vars):
        nA, nB = vars
        m = 10
        M1 = 5.4
        M2 = 31.2
        N = nA + nB
        eq1 = m * nA / N - M1
        eq2 = m * nA * (nB*(m-1) + nA*(N-1)) / (N*(N-1)) - M2
        return [eq1, eq2]
    
    nA4, nB4 = fsolve(equations4, (15, 25))
    
    # 5. Распределение кратности звезд
    M1_5 = 1.6
    q5 = (M1_5 - 1) / M1_5
    
    # 6. Равномерное распределение
    M1_6 = 0.78
    M2_6 = 1.46
    a6 = M1_6 - np.sqrt(3 * (M2_6 - M1_6**2))
    b6 = M1_6 + np.sqrt(3 * (M2_6 - M1_6**2))
    
    # 7. Показательное распределение
    M1_7 = 0.69
    lambda7 = 1 / M1_7
    
    # 8. Гамма-распределение
    M1_8 = 1.72
    t8 = M1_8
    
    # 9. Распределение Лапласа
    M1_9 = 0.178
    lambda9 = 1 / M1_9
    
    # 10. Распределение Парето
    def equations10(vars):
        a, alpha = vars
        M1 = 1.54
        M2 = 2.44
        eq1 = alpha * a / (alpha - 1) - M1 if alpha > 1 else -M1
        eq2 = alpha * a**2 / (alpha - 2) - M2 if alpha > 2 else -M2
        return [eq1, eq2]
    
    a10, alpha10 = fsolve(equations10, (1, 5))
    
    return {
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

results = solve_moments()
for dist_num, params in results.items():
    print(f"Распределение {dist_num}: {params}")