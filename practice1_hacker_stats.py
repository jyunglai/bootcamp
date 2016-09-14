import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import bootcamp_utils

#Create config for mathplotlib rc params
rc = {'lines.linewidth': 2, 'axes.labelsize': 18, 'axes.titlesize': 18}
sns.set(rc=rc)


def draw_bs_reps(data, func, size=1):
    """
    Return bootstrap replicates created from data and desired statistical
    function from n number of replicates
    """
    n = len(data) #Length of input data array
    reps = np.empty(size) #Initialize the array of replicates

    for i in range(size):
        bs_sample = np.random.choice(data, replace=True, size=n)
        reps[i] = func(bs_sample)

    return reps

# #TESTING
# #Load in the data
# bd_1975 = np.loadtxt('data/beak_depth_scandens_1975.csv')
# bd_2012 = np.loadtxt('data/beak_depth_scandens_2012.csv')
#
# #Test draw_bs_reps
# print(draw_bs_reps(bd_1975, np.mean, size=10000))
# print(draw_bs_reps(bd_1975, np.std, size=10000))
