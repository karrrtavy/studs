import numpy as np
from scipy.stats import norm
from scipy.optimize import root_scalar

def solve_probability_problems():
    results = {}

    # Задача 7: Экспоненциальное распределение
    def F7(x): 
        return np.where(x >= 0, 1 - np.exp(-x), 0)
    results[7] = solve_problem(F7, c=2.5, a=-0.5, b=1, p=0.96)
        
    return results

def solve_problem(F, c, a, b, p):
    # Часть а) Вероятность P(ξ - a < c < ξ + b)
    def prob_a(F, c, a, b):
        if a == 0:
            return F(c + b) - F(c)
        elif b == 0:
            return F(c) - F(c - a)
        else:
            return F(c + b) - F(c - a)
    
    p_a = prob_a(F, c, a, b)
    
    # Часть б) Нахождение a и b с условием симметрии
    def equation_b(t, F, c, p):
        a_val = t
        b_val = t  # Для симметричного случая
        return prob_a(F, c, a_val, b_val) - p
    
    # Находим корень уравнения
    try:
        sol = root_scalar(equation_b, args=(F, c, p), bracket=[0, 10], method='brentq')
        t = sol.root
        a_b = t
        b_b = t
    except:
        # Если симметричное решение не подходит, ищем общий случай
        def equation_b_general(t, F, c, p):
            a_val = t[0]
            b_val = t[1]
            return prob_a(F, c, a_val, b_val) - p
        
        from scipy.optimize import least_squares
        sol = least_squares(equation_b_general, x0=[1, 1], args=(F, c, p))
        a_b, b_b = sol.x
    
    return {
        'a)': round(p_a, 5),
        'б)': (f'(ξ - {round(a_b, 5)}, ξ + {round(b_b, 5)})')
    }

results = solve_probability_problems()

for problem, solution in results.items():
    print(f"Задача {problem}:")
    print(f"  a) {solution['a)']}")
    print(f"  б) {solution['б)']}")
    print()