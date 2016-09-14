import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import bootcamp_utils
sns.set()

bd_1975 = np.loadtxt('data/beak_depth_scandens_1975.csv')
bd_2012 = np.loadtxt('data/beak_depth_scandens_2012.csv')

x_1975, y_1975 = bootcamp_utils.ecdf(bd_1975)
x_2012, y_2012 = bootcamp_utils.ecdf(bd_2012)

plt.plot(x_1975, y_1975, marker='.', linestyle='none')
plt.plot(x_2012, y_2012, marker='.', linestyle='none')
plt.xlabel('beak depth (mm)')
plt.ylabel('ECDF')

plt.show()
