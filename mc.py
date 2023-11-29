import numpy as np
import matplotlib.pyplot as plt

def estimate_pi_vectorized(num_samples):
    x = np.random.uniform(-1, 1, num_samples)
    y = np.random.uniform(-1, 1, num_samples)

    inside_circle = np.sum(x**2 + y**2 <= 1)
    proportion = inside_circle / num_samples
    return proportion * 4

true_pi = np.pi
sample_sizes = np.arange(100, 100001, 10)
errors = []

for size in sample_sizes:
    pi_estimate = estimate_pi_vectorized(size)
    error = pi_estimate - true_pi
    errors.append(error)
    print(f"Sample size: {size}, Estimated pi: {pi_estimate}, Error: {error}")


# Plotting as a line plot
plt.plot(sample_sizes, errors, label='Error', marker='o', linestyle='-', markersize=3)
plt.axhline(0, color='black', linewidth=0.5, linestyle='--', label='True Value')
plt.xlabel('Sample Size')
plt.ylabel('Error')
plt.title('Monte Carlo Estimation of Pi - Error vs. Sample Size')
plt.legend()

# Adjust y-axis limits for better visualization
plt.ylim(-0.1, 0.1)

plt.show()
# import random
# import math
# import matplotlib.pyplot as plt
# def estimate_pi(num_samples):
#     circle = 0
#     for _ in range(num_samples):
#         x = random.uniform(-1, 1)
#         y = random.uniform(-1, 1)

#         if x**2 + y**2 <= 1:
#             circle += 1

#     proportion = circle / num_samples
#     return proportion * 4

# true_pi = math.pi
# sample_sizes = list(range(100, 10001,10))
# errors = []

# # Adjust the range and step size according to your needs
# for size in sample_sizes:
#     pi_estimate = estimate_pi(size)
#     error = abs(pi_estimate - true_pi)
#     errors.append(error)
#     print(f"Sample size: {size}, Estimated pi: {pi_estimate}, Error: {error}")

# # Plotting
# plt.plot(sample_sizes, errors, label='Error')
# plt.axhline(0, color='black', linewidth=0.5, linestyle='--', label='True Value')
# plt.xlabel('Sample Size')
# plt.ylabel('Error')
# plt.title('Monte Carlo Estimation of Pi - Error vs. Sample Size')
# plt.legend()
# plt.show()
        