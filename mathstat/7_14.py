import numpy as np
from scipy.optimize import minimize

def solve_adjustment():    
    # Задача 7
    x7 = np.array([1.21, 3.11, 11.1])
    sigma7 = np.array([0.01, 0.01, 0.02])
    def constraint7(x):
        return x[2] - x[0]**2 - x[1]**2
    result7 = adjust_measurements(x7, sigma7, constraint7)
    
    return {
        7: result7,
    }

def adjust_measurements(x_initial, sigmas, constraint):
    def objective(x):
        return np.sum(((x - x_initial) / sigmas) ** 2)
    
    cons = {'type': 'eq', 'fun': constraint}
    
    result = minimize(objective, x_initial, constraints=cons)
    return np.round(result.x, 5)

results = solve_adjustment()

for problem, solution in results.items():
    print(f"Задача {problem}: {solution}")