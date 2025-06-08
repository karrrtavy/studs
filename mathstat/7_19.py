from scipy.stats import chi2

chi_squared = 0.7
df = 3  # Степени свободы (k - 1 - m)
alpha_max = 1 - chi2.cdf(chi_squared, df)

print(f"χ² = {chi_squared:.2f}, α_max = {alpha_max:.8f}")