from scipy.stats import poisson

# Given average rate of calls per hour (lambda)
lambda_rate = 4

# a) Calculate the probability of receiving 3 or fewer calls
prob_3_or_fewer = poisson.cdf(3, lambda_rate)
print(f"Probability of receiving 3 or fewer calls: {prob_3_or_fewer:.4f}")

# b) Calculate the probability of receiving 4 or more calls
prob_4_or_more = 1 - prob_3_or_fewer
print(f"Probability of receiving 4 or more calls: {prob_4_or_more:.4f}")
