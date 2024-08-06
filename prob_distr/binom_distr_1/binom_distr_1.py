from scipy.stats import binom

# Parameters
n = 20  # Number of trials
p = 0.06  # Probability of success
k = 2  # Number of successes

# Calculate the cumulative probability of at most k successes
cumulative_probability = binom.cdf(k, n, p)

print(f"The probability that at most {k} out of {n} components are defective is: {cumulative_probability:.6f}")
