import numpy as np
import matplotlib.pyplot as plt

def threedoor_simulation_optimized(num_samples):
    not_change_door_win = 0
    change_door_win = 0
    not_win = 0

    # Simulate all samples at once
    x = np.random.randint(1, 4, num_samples)
    y = np.random.randint(1, 4, num_samples)
    change = np.random.randint(0, 2, num_samples)

    # Check conditions using vectorized operations
    not_change_door_win += np.sum((x == y) & (change == 0))
    change_door_win += np.sum((x != y) & (change == 1))
    not_win += np.sum((x == y) & (change == 1)) + np.sum((x != y) & (change == 0))

    not_change_door_win_rate = not_change_door_win / num_samples
    change_door_win_rate = change_door_win / num_samples
    not_win_rate = not_win / num_samples

    print(f"Not changing door win count: {not_change_door_win}")
    print(f"Changing door win count: {change_door_win}")
    print(f"Not winning count: {not_win}")

    print(f"Not changing door win rate: {not_change_door_win_rate}")
    print(f"Changing door win rate: {change_door_win_rate}")
    print(f"Not winning rate: {not_win_rate}")

    return not_change_door_win_rate, change_door_win_rate, not_win_rate

sample_sizes = np.arange(100, 100001, 10)

not_change_door_win_rates = []
change_door_win_rates = []
not_win_rates = []

for size in sample_sizes:
    not_change_door_win_rate, change_door_win_rate, not_win_rate = threedoor_simulation_optimized(size)
    not_change_door_win_rates.append(not_change_door_win_rate)
    change_door_win_rates.append(change_door_win_rate)
    not_win_rates.append(not_win_rate)

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(sample_sizes, not_change_door_win_rates, label='Not Changing Door Win Rate')
plt.axhline(y=1/6, color='r', linestyle='--', label='Theoretical Probability (1/6) - Not Changing Door')

plt.plot(sample_sizes, change_door_win_rates, label='Changing Door Win Rate')
plt.axhline(y=1/3, color='g', linestyle='--', label='Theoretical Probability (1/3) - Changing Door')

plt.plot(sample_sizes, not_win_rates, label='Not Winning Rate')
plt.axhline(y=1/2, color='b', linestyle='--', label='Theoretical Probability (1/2) - Not Winning')

plt.title('Monty Hall Simulation Results')
plt.xlabel('Number of Simulations')
plt.ylabel('Winning Rate')
plt.legend(loc='upper center', bbox_to_anchor=(0.5, 1.15), ncol=3)
plt.xscale('log')  # Use logarithmic scale for better visualization

plt.show()