# Define the uniform distribution parameters
a = 10
b = 20

# a) Calculate the probability of manufacturing time between 12 and 15 minutes
x1 = 12
x2 = 15
prob_12_to_15 = (x2 - x1) / (b - a)
print(f"Probability of manufacturing time between 12 and 15 minutes: {prob_12_to_15:.4f}")

# b) Calculate the expected time to manufacture a widget
expected_time = (a + b) / 2
print(f"Expected time to manufacture a widget: {expected_time:.2f} minutes")
