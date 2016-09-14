import numpy as np
import scipy.special
import matplotlib.pyplot as plt
import seaborn as sns

# Set matplotlib rc params.
rc = {'lines.linewidth' : 2, 'axes.labelsize' : 18,
        'axes.titlesize' : 18}
sns.set(rc=rc)

def bohr_parameter(c, RK, KdA=0.017, KdI=0.002, Kswitch=5.8):
    """Computes the bohr parameter from a set of IPTG concentrations"""
    numerator = (1 + c/KdA) ** 2
    denominator = (1 + c/KdA) ** 2 + Kswitch * (1 + c/KdI) ** 2
    return -np.log(RK) - np.log(numerator/denominator)

def fold_change_bohr(bohr_parameter):
    """Computes fold change using the bohr parameter"""
    return 1/(1 + np.exp(-bohr_parameter))

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

RK_wt = 141.5
RK_q18m = 1332
RK_q18a = 16.56

# Plot theoretical bohr fold change vs. bohr param curve:
bohr_params_x = np.linspace(-6,7,num=100)
theoretical_fc_y = fold_change_bohr(bohr_params_x)
plt.plot(bohr_params_x, theoretical_fc_y, color='gray')

# Compute bohr parameter for experimental data:
wt_bohr_param = bohr_parameter(wt_iptg, RK_wt)
q18m_bohr_param = bohr_parameter(q18m_iptg, RK_q18m)
q18a_bohr_param = bohr_parameter(q18a_iptg, RK_q18a)

# Plot data in logscale
plt.plot(wt_bohr_param, wt_fc, marker='.', markersize=20,
             linestyle='none', color='blue', alpha=0.5)
plt.plot(q18a_bohr_param, q18a_fc, marker='.', markersize=20,
             linestyle='none', color='red', alpha=0.5)
plt.plot(q18m_bohr_param, q18m_fc, marker='.', markersize=20,
             linestyle='none', color='green', alpha=0.5)

plt.legend(('theoretical','wt', 'q18a', 'q18m'), loc='upper left')
plt.xlabel('Bohr Parameter')
plt.ylabel('Fold Change')
plt.margins(0.05)

plt.savefig('exercise3.2f_bohrParam.svg', bbox_inches='tight')

plt.show()
