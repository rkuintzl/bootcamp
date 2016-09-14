import numpy as np
import scipy.special
import matplotlib.pyplot as plt
import seaborn as sns

# Set matplotlib rc params.
rc = {'lines.linewidth' : 2, 'axes.labelsize' : 18,
        'axes.titlesize' : 18}
sns.set(rc=rc)

# Params for exercise 3.3a:
alpha = 1
beta = 0.2
delta = 0.3
gamma = 0.8
delta_t = 0.001
t = np.arange(0, 60, delta_t)
r = np.empty_like(t)
f = np.empty_like(t)
r[0] = 10
f[0] = 1

for i in range(1, len(t)):
    r[i] = r[i-1] + delta_t * (alpha * r[i-1] - beta * f[i-1] * r[i-1])
    f[i] = f[i-1] + delta_t * (delta * f[i-1] * r[i-1] - gamma * f[i-1])

plt.plot(t, r)
plt.plot(t, f)
plt.margins(0.02)
plt.xlabel('time')
plt.ylabel('number of animals')

plt.legend(('rabbits','foxes'), loc='upper right')

plt.savefig('exercise3.3_difEQs.svg', bbox_inches='tight')

plt.show()
