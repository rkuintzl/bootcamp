import numpy as np
import scipy.special
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set matplotlib rc params.
rc = {'lines.linewidth' : 2, 'axes.labelsize' : 18,
        'axes.titlesize' : 18}
sns.set(rc=rc)

# Load the data
df = pd.read_csv('data/frog_tongue_adhesion.csv', comment='#')

# Extract the impact time of all impacts that had
# # an adhesive strength of magnitude greater than 2000 Pa.
# df_t_adhs_2000Pa = df.loc[df['adhesive strength (Pa)'] < -2000, ['impact time (ms)']]
#
# # Extract the impact force and adhesive force for all of Frog II's strikes.
# df_frog2_impf_adhf = df.loc[df['ID']=='II', ['impact force (mN)', 'adhesive force (mN)']]
#
# # Extract the adhesive force and the time the frog pulls on the target
# # for juvenile frogs (Frogs III and IV).
# df_juv_adhf_time = df.loc[(df['ID']=='III') | (df['ID']=='IV'),
#                          ['impact time (ms)', 'adhesive force (mN)']]


def retrieve_impact_force(frog_id,col_header):
    """Retrieves impact forces for all experiments with a specified frog."""
    df_subset = df.loc[df['ID']==frog_id,[col_header]]
    return df_subset

frogs = ('I','II','III','IV')

array_impf_mean = np.empty(4) # CCan I do this?
for i, frog in enumerate(frogs):
    col_header = 'impact force (mN)'
    df_impf = retrieve_impact_force(frog,col_header)
    impf_mean = retrieve_impact_force(frog,col_header).mean()
    array_impf_mean[i] = impf_mean[0]

print(array_impf_mean)

# Try grouby

#def coeff_of_var(data):


# We only want ID's and impact forces, so slice those out
# df_impf = df.loc[:, ['ID', 'impact force (mN)']]
#
# # Make a GroupBy object
# grouped = df_impf.groupby('ID')
#
# # Apply the np.mean function to the grouped object
# df_mean_impf = grouped.apply(np.mean)
# df_mean_med_impf = grouped.agg([np.mean, np.median, np.std])



#plt.plot(df['impact force (mN)'], df['adhesive force (mN)'], marker='.',
#         linestyle='none')
# plt.clf()
# df.plot(x='total contact area (mm2)', y='adhesive force (mN)', kind='scatter')
# plt.xlabel('total contact area (mm2)')
# plt.ylabel('adhesive force (mN)')
# plt.show()
