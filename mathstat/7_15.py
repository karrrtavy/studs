import numpy as np
from scipy.stats import norm
from scipy.optimize import root_scalar

def solve_probability_problems():
    results = {}
    
    # Задача 1: F(x) = Φ(x), c = 0.5
    def F1(x): return norm.cdf(x)
    results[1] = solve_problem(F1, c=0.5, a=0, b=1, p=0.98)
    
    # Задача 2: F(x) = Φ(2x+3), c = -1
    def F2(x): return norm.cdf(2*x + 3)
    results[2] = solve_problem(F2, c=-1, a=1, b=0.5, p=0.98)
    
    # Задача 3: F(x) = Φ(x-1), c = 3
    def F3(x): return norm.cdf(x - 1)
    results[3] = solve_problem(F3, c=3, a=0, b=2, p=0.96)
    
    # Задача 4: F(x) = Φ(0.2x-2), c = 2
    def F4(x): return norm.cdf(0.2*x - 2)
    results[4] = solve_problem(F4, c=2, a=0, b=1, p=0.97)
    
    # Задача 5: F(x) = Φ(0.3x+0.7), c = 1
    def F5(x): return norm.cdf(0.3*x + 0.7)
    results[5] = solve_problem(F5, c=1, a=0.5, b=0, p=0.95)
    
    # Задача 6: F(x) = arctg(x)/π + 1/2, c = 3
    def F6(x): return np.arctan(x)/np.pi + 0.5
    results[6] = solve_problem(F6, c=3, a=0.5, b=1, p=0.96)
    
    # Задача 7: Экспоненциальное распределение
    def F7(x): 
        return np.where(x >= 0, 1 - np.exp(-x), 0)
    results[7] = solve_problem(F7, c=2.5, a=-0.5, b=1, p=0.96)
    
    # Задача 8: Равномерное распределение
    def F8(x): 
        return np.piecewise(x, [x < 0, (0 <= x) & (x <= 1), x > 1], 
                           [0, lambda x: x, 1])
    results[8] = solve_problem(F8, c=1.2, a=-0.4, b=1, p=0.94)
    
    # Задача 9: Смесь экспоненциальных распределений
    def F9(x): 
        return np.piecewise(x, [x <= 0, x > 0], 
                           [lambda x: np.exp(x)/2, lambda x: 1 - np.exp(-x)/2])
    results[9] = solve_problem(F9, c=1, a=1, b=3, p=0.95)
    
    # Задача 10: Гамма-распределение (k=2)
    def F10(x): 
        return np.where(x > 0, 1 - (x + 1)*np.exp(-x), 0)
    results[10] = solve_problem(F10, c=1, a=1, b=2, p=0.97)
    
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