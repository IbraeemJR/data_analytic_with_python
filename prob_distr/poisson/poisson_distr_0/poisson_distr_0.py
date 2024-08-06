from scipy.stats import poisson

# Parameters
lambda_value = 3.2  # Average rate of customers
k = 5  # Number of customers

# Calculate Poisson PMF
probability = poisson.pmf(k, lambda_value)

print(f"The probability that exactly {k} customers arrive in a 4-minute interval is: {probability:.4f}")
