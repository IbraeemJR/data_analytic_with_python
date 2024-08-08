from scipy.stats import binom

# Parameters
n = 20  # Number of trials
p = 0.4  # Probability of success
k = 10  # Number of successes

# Calculate the probability of exactly k successes
probability = binom.pmf(k, n, p)

print(f"The probability that exactly {k} out of {n} users will find the feature useful is: {probability:.6f}")
