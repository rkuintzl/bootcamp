import numpy as np
import scipy.special
import matplotlib.pyplot as plt
import seaborn as sns

# Set matplotlib rc params.
rc = {'lines.linewidth' : 2, 'axes.labelsize' : 18,
        'axes.titlesize' : 18}
sns.set(rc=rc)

def ecdf(data):
    """
    Compute x, y values for an empirical cumulative distribution function.
    """
    x = np.sort(data)
    y = np.arange(1, 1+len(x)) / len(x)

    return x, y

# Close all other plots just in case
plt.close()

# Load the food data
xa_high = np.loadtxt('data/xa_high_food.csv')
xa_low = np.loadtxt('data/xa_low_food.csv')

x_high, y_high = ecdf(xa_high)
x_low, y_low = ecdf(xa_low)

x = np.linspace(1600, 2500, 400) # xrange min, xrange max, number of points
cdf_high = scipy.stats.norm.cdf(x, loc=np.mean(xa_high), scale = np.std(xa_high))
cdf_low = scipy.stats.norm.cdf(x, loc=np.mean(xa_low), scale = np.std(xa_low))

# Plot data
plt.plot(x_low, y_low, marker='.', markersize=20, alpha=0.5)
plt.plot(x_high, y_high, marker='.', markersize=20, alpha=0.5)
# Plot smoothed points
plt.plot(x, cdf_low, color='gray')
plt.plot(x, cdf_high, color='gray')

plt.legend(('low food', 'high food'), loc='lower right')
# plt.errorbar(iptg, gfp, yerr=sem, marker='.',
#             markersize=20)
plt.xlabel('Cross-sectional area (µm)')
plt.ylabel('eCDF')

plt.savefig('lesson24_egg_area_eCDF.svg', bbox_inches='tight')

plt.show()
# plt.margins(0.05)
