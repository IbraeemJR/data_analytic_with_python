from scipy.stats import binom

# Parameters
n = 25  # Number of trials
p = 0.65  # Probability of success
k = 19  # Number of successes

# Calculate the probability of exactly k successes
probability = binom.pmf(k, n, p)

print(f"The probability that exactly {k} out of {n} bulbs will pass is: {probability:.6f}")
