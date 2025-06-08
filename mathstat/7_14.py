import numpy as np
from scipy.optimize import minimize

def solve_adjustment():
    # Задача 1
    x1 = np.array([17, 84, 83])
    sigma1 = np.array([1, 1, 1])
    def constraint1(x):
        return x[0] + x[1] + x[2] - 180
    result1 = adjust_measurements(x1, sigma1, constraint1)
    
    # Задача 2
    x2 = np.array([52, 47, 82])
    sigma2 = np.array([1, 2, 1.5])
    result2 = adjust_measurements(x2, sigma2, constraint1)
    
    # Задача 3
    x3 = np.array([0.27, 0.15, 0.57])
    sigma3 = np.array([0.02, 0.03, 0.01])
    def constraint3(x):
        return x[0] + x[1] + x[2] - 1
    result3 = adjust_measurements(x3, sigma3, constraint3)
    
    # Задача 4
    x4 = np.array([0.89, 0.46])
    sigma4 = np.array([0.01, 0.01])
    def constraint4(x):
        return x[0]**2 + x[1]**2 - 1
    result4 = adjust_measurements(x4, sigma4, constraint4)
    
    # Задача 5
    x5 = np.array([0.27, 0.53, 0.80])
    sigma5 = np.array([0.01, 0.01, 0.01])
    def constraint5(x):
        return x[0]**2 + x[1]**2 + x[2]**2 - 1
    result5 = adjust_measurements(x5, sigma5, constraint5)
    
    # Задача 6
    x6 = np.array([0.89, 0.46])
    sigma6 = np.array([0.01, 0.02])
    result6 = adjust_measurements(x6, sigma6, constraint4)
    
    # Задача 7
    x7 = np.array([1.21, 3.11, 11.1])
    sigma7 = np.array([0.01, 0.01, 0.02])
    def constraint7(x):
        return x[2] - x[0]**2 - x[1]**2
    result7 = adjust_measurements(x7, sigma7, constraint7)
    
    # Задача 8
    x8 = np.array([3.14, 1.21, 8.40])
    sigma8 = np.array([0.01, 0.01, 0.02])
    def constraint8(x):
        return x[2] - x[0]**2 + x[1]**2
    result8 = adjust_measurements(x8, sigma8, constraint8)
    
    # Задача 9
    x9 = np.array([2.17, 1.34, 2.90])
    sigma9 = np.array([0.01, 0.02, 0.03])
    def constraint9(x):
        return x[2] - x[0]*x[1]
    result9 = adjust_measurements(x9, sigma9, constraint9)
    
    # Задача 10
    x10 = np.array([3.12, 2.87, 8.95])
    sigma10 = np.array([0.02, 0.01, 0.03])
    result10 = adjust_measurements(x10, sigma10, constraint9)
    
    return {
        1: result1, 2: result2, 3: result3, 4: result4, 5: result5,
        6: result6, 7: result7, 8: result8, 9: result9, 10: result10
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