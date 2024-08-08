# Define the uniform distribution parameters
a = 30
b = 60

# a) Calculate the probability of delivery time being 45 minutes or less
x = 45
prob_less_than_45 = (x - a) / (b - a)
print(f"Probability of delivery time being 45 minutes or less: {prob_less_than_45:.4f}")

# b) Calculate the probability of delivery time being between 50 and 55 minutes given it exceeds 50 minutes
prob_50_to_55_given_gt_50 = (55 - 50) / (b - 50)
print(f"Probability of delivery time being between 50 and 55 minutes given it exceeds 50 minutes: {prob_50_to_55_given_gt_50:.4f}")
