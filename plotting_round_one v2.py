import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Set matplotlib rc params.
rc = {'lines.linewidth' : 2, 'axes.labelsize' : 18,
        'axes.titlesize' : 18}
sns.set(rc=rc)

# Load the food data
xa_high = np.loadtxt('data/xa_high_food.csv')
xa_low = np.loadtxt('data/xa_low_food.csv')

# Make bin boundaries
global_min = np.min([np.min(xa_low),np.min(xa_high)])
global_max = np.max([np.max(xa_low),np.max(xa_high)])

bins = np.arange(global_min-50, global_max+50, 50)

# Plot the data as two overlaid histograms:
_ = plt.hist(xa_low, normed=True, bins=bins, histtype='stepfilled', alpha=0.5)
_ = plt.hist(xa_high, normed=True, bins=bins, histtype='stepfilled', alpha=0.5)
plt.xlabel('Cross-sectional area (µm$^2$)')
plt.ylabel('frequency')
plt.legend(('low concentration', 'high concentration'), loc='upper right')

# Save the figure
plt.savefig('lesson21_egg_area_hist.svg', bbox_inches='tight')

# Show the figure
plt.show()
