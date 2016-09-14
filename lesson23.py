import numpy as np
import scipy.special
import matplotlib.pyplot as plt
import seaborn as sns

# Set matplotlib rc params.
rc = {'lines.linewidth' : 2, 'axes.labelsize' : 18,
        'axes.titlesize' : 18}
sns.set(rc=rc)

# Processing the spike data.
data = np.loadtxt('data/collins_switch.csv', skiprows=2, delimiter=',')

iptg = data[:,0]
gfp = data[:,1] # foldchange
sem = data[:,2]

x_min = min(iptg)
x_max = max(iptg)

# Close all other plots just in case
plt.close()

# Plot data
plt.errorbar(iptg, gfp, yerr=sem, marker='.',
            markersize=20)
plt.xlabel('IPTG (mM)')
plt.ylabel('GFP Fluorescence')
plt.margins(0.05)
plt.xlim(x_min-1, x_max+1)
plt.show()
