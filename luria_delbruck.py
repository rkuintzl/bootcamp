import numpy as np
import scipy.special
import matplotlib.pyplot as plt
import bootcamp_utils
import seaborn as sns

# Set matplotlib rc params.
rc = {'lines.linewidth' : 2, 'axes.labelsize' : 18,
        'axes.titlesize' : 18}
sns.set(rc=rc)

# Specify parameters
n_gen = 16  # number of generation
r = 1e-5    # chance of having a beneficial mutation (probability of success)
n_cells = 2 ** (n_gen - 1)  # total number of cells


# Adaptive immunity: binomial distribution
ai_samples = np.random.binomial(n_cells, r, size=100000)

# Report mean and std
print('AI mean:', np.mean(ai_samples))
print('AI std:', np.std(ai_samples))
print('AI Fano:', np.var(ai_samples) / np.mean(ai_samples))


# Function to draw out of random muation hypothesis
def draw_random_mutation(n_gen, r):
    """Draw sample under random mutation hypothesis."""
    # Initialize number of mutations
    n_mut = 0

    for g in range(n_gen):
        n_remaining = (2 ** (g - 1) - n_mut) * 2 # number of cells that can get mutations
        n_mut = 2 * n_mut + np.random.binomial(n_remaining, r)

    return n_mut

def sample_random_mutation(n_gen, r, size=1):
    """Sample out of the Luria-Delbruck (Jackpot) distribution"""
    # Initialize samples
    samples = np.empty(size)

    # Draw the samples
    for i in range(size):
        samples[i] = draw_random_mutation(n_gen, r)

    return samples

#ai_samples = draw_random_mutation(n_gen, r)
# x_ai, y_ai = bootcamp_utils.ecdf(ai_samples)
rm_samples = sample_random_mutation(n_gen, r, size=100000)
x_rm, y_rm = bootcamp_utils.ecdf(rm_samples)

# Report mean and std
print('RM mean:', np.mean(rm_samples))
print('RM std:', np.std(rm_samples))
print('RM Fano:', np.var(rm_samples) / np.mean(rm_samples))

# Fano factor ~= 1 if AI
# Fano factor >> 1 if RM

# plt.plot(x_ai, y_ai)
plt.semilogx(x_rm, y_rm, linestyle='none', marker='.')

# Clean up plot
plt.margins(y=0.02)
plt.xlabel('number of survivors')
plt.ylabel('CDF')

plt.show()
