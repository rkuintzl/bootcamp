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

df = df.rename(columns={'impact force (mN)': 'impf'})

# Get stats on all four frogs at once without a loop!
gb_frog = df.groupby('ID')
mean_impf = gb_frog['impf'].mean()
sem_impf = gb_frog['impf'].sem()  # is this sample or population? which SHOULD it be?

print(mean_impf)
print(sem_impf)

# These operations work on a tidy data frame
#sns.barplot(data=df, x='ID', y ='impf')
#sns.swarmplot(data=df, x='ID', y ='impf', hue='date')
#plt.gca().legend_.remove() # removes the legend
sns.boxplot(data=df, x='ID', y ='impf') # need to remove color and narrow boxes

plt.show()
