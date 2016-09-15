import numpy as np
import scipy.optimize
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Set matplotlib rc params.
rc = {'lines.linewidth' : 2, 'axes.labelsize' : 18,
        'axes.titlesize' : 18}
sns.set(rc=rc)

def gradient_model(x, I_0, a, lam):
    """Model for Bcd gradient: exponential decay plus background"""

    if not np.all(np.array(x) >= 0):
        raise RuntimeError('All values of x must be >= 0.')
    if not np.all(np.array([I_0, a, lam]) >= 0):
        raise RuntimeError('All parameters must be >= 0.')

    return a + I_0 * np.exp(-x/lam)

# Load data, rename column headers
df = pd.read_csv('data/bcd_gradient.csv', comment='#')
df = df.rename(columns={'fractional distance from anterior': 'x',
                 '[bcd] (a.u.)': 'I_bcd'})

# Specify initial guess
a_guess = 0.2
I_0_guess = 0.9 - a_guess
lam_guess = 0.25  # x value corresponding to 1/3 of max y-value

# Construct initial guess array
p0 = np.array([I_0_guess, a_guess, lam_guess])

# Do curve fit, but dump covariance into dummy variable
p_opt, _ = scipy.optimize.curve_fit(gradient_model, df['x'], df['I_bcd'], p0=p0)

# Print the results
# print("""
# I_0 = {0:.2f}
#   a = {1:.2f}
#   λ = {2:.2f}
# """.format(*tuple(p)))

# Smooth x values (100 values between zero and one)
x_smooth = np.linspace(0, 1, 100)

# Compute smooth curve
I_smooth = gradient_model(x_smooth, *tuple(p_opt)) # *tuple contains (I_0, a, lam)

# Plot everything together
plt.plot(x_smooth, I_smooth, marker='None', linestyle='-', color='gray')
plt.plot(df['x'], df['I_bcd'], marker='.', linestyle='none')

# Label axes
plt.xlabel('$x$') # dimensionless
plt.ylabel('$I$ (a.u.)')

plt.show()
