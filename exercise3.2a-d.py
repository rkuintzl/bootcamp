import numpy as np
import scipy.special
import matplotlib.pyplot as plt
import seaborn as sns

# Set matplotlib rc params.
rc = {'lines.linewidth' : 2, 'axes.labelsize' : 18,
        'axes.titlesize' : 18}
sns.set(rc=rc)

def theoretical_fold_change(c, RK, KdA=0.017, KdI=0.002, Kswitch=5.8):
    """Computes theoretical fold change"""
    numerator = RK * (1 + (c/KdA) ** 2)
    denominator = (1 + c/KdA) ** 2 + Kswitch * (1 + c/KdI) ** 2
    inverse_fc = 1 + (numerator/denominator)
    return inverse_fc ** -1

# Close all other plots just in case
plt.close()

# Load the data
wt_lac = np.loadtxt('data/wt_lac.csv', delimiter = ',', skiprows=3)
q18m_lac = np.loadtxt('data/q18m_lac.csv', delimiter = ',', skiprows=3)
q18a_lac = np.loadtxt('data/q18a_lac.csv', delimiter = ',', skiprows=3)

wt_iptg = wt_lac[:,0]
wt_fc = wt_lac[:,1]
q18m_iptg = q18m_lac[:,0]
q18m_fc = q18m_lac[:,1]
q18a_iptg = q18a_lac[:,0]
q18a_fc = q18a_lac[:,1]

# Create theoretical fold change curves
RK_wt = 141.5
RK_q18m = 1332
RK_q18a = 16.56

smooth_iptg = np.logspace(-6, 2, num=100, base=10)

wt_theor_fc = theoretical_fold_change(smooth_iptg, RK_wt) # can I pass only the two non-keyword terms?
q18m_theor_fc = theoretical_fold_change(smooth_iptg, RK_q18m)
q18a_theor_fc = theoretical_fold_change(smooth_iptg, RK_q18a)

# Plot theoretical fold change curves:
plt.semilogx(smooth_iptg, wt_theor_fc, color='blue')
plt.semilogx(smooth_iptg, q18a_theor_fc, color='red')
plt.semilogx(smooth_iptg, q18m_theor_fc, color='green')

# Plot data in logscale
plt.semilogx(wt_iptg, wt_fc, marker='.', markersize=20,
             linestyle='none', color='blue', alpha=0.5)
plt.semilogx(q18a_iptg, q18a_fc, marker='.', markersize=20,
             linestyle='none', color='red', alpha=0.5)
plt.semilogx(q18m_iptg, q18m_fc, marker='.', markersize=20,
             linestyle='none', color='green', alpha=0.5)

plt.legend(('wt_theor', 'q18a_theor', 'q18m_theor', 'wt', 'q18a', 'q18m'), loc='upper left')
plt.xlabel('IPTG (mM)')
plt.ylabel('Fold Change')
plt.margins(0.05)

plt.savefig('exercise3.2d_theoreticalFoldChange.svg', bbox_inches='tight')

plt.show()
