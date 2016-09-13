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

# Plot the data as a histogram:
_ = plt.hist((xa_low, xa_high), bins=bins)
plt.xlabel('Cross-sectional area (µm$^2$)')
plt.ylabel('count', rotation='horizontal')
plt.show()
