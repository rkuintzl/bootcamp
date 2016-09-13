import numpy as np
import scipy.special
import matplotlib.pyplot as plt
import seaborn as sns

# Generate an array of x values
x = np.linspace(-15, 15, 400)

# Compute the normalized intensity
norm_I = 4 * (scipy.special.j1(x) / x) ** 2

# Set matplotlib rc params.
rc = {'lines.linewidth' : 2, 'axes.labelsize' : 18,
        'axes.titlesize' : 18}
sns.set(rc=rc)

# Plot our computation:
plt.plot(x, norm_I, marker='.', linestyle='none')
plt.margins(0.02)
plt.xlabel('$x$')
plt.ylabel('$I(x) / I_0$')

# Processing the spike data.
data = np.loadtxt('data/retina_spikes.csv', skiprows=2, delimiter=',')
time = data[:,0] # everything in first column
Voltage = data[:,1]

# Close all other plots just in case
plt.close()

# Plot spike data
plt.plot(time,Voltage)
plt.xlabel('time (ms)')
plt.ylabel('Voltage (µV)')
plt.xlim(1395, 1400)
plt.show()

#plt.legend(('low concentration', 'high concentration'), loc='upper right')

# Save the figure
#plt.savefig('lesson21_egg_area_hist.svg', bbox_inches='tight')

# Show the figure
plt.show()
