import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import bootcamp_utils
sns.set()

bd_1975 = np.loadtxt('data/beak_depth_scandens_1975.csv')
bd_2012 = np.loadtxt('data/beak_depth_scandens_2012.csv')

def draw_boostrap_reps(data, n_reps=100000, param='mean'):
    """Generate bootstrap for 1975"""
    bs_replicates = np.empty(n_reps)
    for i in range(n_reps):
        bs_sample = np.random.choice(bd_1975, replace=True, size = len(bd_1975))
        if param == 'mean':
            bs_replicates[i] = np.mean(bs_sample)
        elif param == 'std':
            bs_replicates[i] = np.std(bs_sample)
        else:
            raise RuntimeError("Statistic must be one of 'mean' or 'std'.")
    return bs_replicates, np.mean(bs_replicates), np.percentile(bs_replicates, [2.5, 97.5])

bs_replicates_1975, bs_mean_1975, conf_int_1975 = draw_boostrap_reps(bd_1975)
bs_replicates_2012, bs_mean_2012, conf_int_2012 = draw_boostrap_reps(bd_2012)


#_ = plt.hist(bs_replicates_1975, bins=100)


# How do you know whether the distributions
# are significantly different based on confidence intervals of the mean?
# What about K-S test?
# What about normal approximation interval? (when data are normal?)
# How tell whether data are normal? How compare to Gaussian curve quantitatively?

# # Compute eCDFs
# x_1975, y_1975 = bootcamp_utils.ecdf(bd_1975)
# x_2012, y_2012 = bootcamp_utils.ecdf(bd_2012)
# x_1975_bs, y_1975_bs = bootcamp_utils.ecdf(bs_sample)
#
# # Plot eCDFs
# plt.plot(x_1975, y_1975, marker='.', linestyle='none')
# plt.plot(x_1975_bs, y_1975_bs, marker='.', linestyle='none')
# # plt.plot(x_2012, y_2012, marker='.', linestyle='none')
# plt.xlabel('beak depth (mm)')
# plt.ylabel('ECDF')
# plt.legend(('1975', '1975 boostrap'), loc='lower right')
#
# plt.show()
