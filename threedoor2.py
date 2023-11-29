import numpy as np
import matplotlib.pyplot as plt

def threedoor_simulation_optimized(num_samples):
    not_change_door_win = 0

    chosen_doors = np.random.randint(1, 4, num_samples)

    # Check conditions using vectorized operations
    not_change_door_win += np.sum(chosen_doors != np.random.randint(1, 4, num_samples))

    not_change_door_win_rate = not_change_door_win / num_samples

    print(f"Not changing door win count: {not_change_door_win / num_samples}")

    return not_change_door_win_rate

sample_sizes = np.arange(100, 100001, 10)

not_change_door_win_rates = []

for size in sample_sizes:
    not_change_door_win_rate = threedoor_simulation_optimized(size)
    not_change_door_win_rates.append(not_change_door_win_rate)

# Plot the results
plt.plot(sample_sizes, not_change_door_win_rates, label="Not changing door")
plt.xlabel("Number of Simulations")
plt.ylabel("Winning Probability")
plt.legend()
plt.show()
