# Define the uniform distribution parameters
a = 27
b = 39

# Define the interval for which we want to find the probability
x1 = 30
x2 = 35

# Calculate the probability of the assembly time being between 30 and 35 seconds
probability = (x2 - x1) / (b - a)
print(f"Probability that the assembly time is between 30 and 35 seconds: {probability:.4f}")
