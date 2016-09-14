import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import bootcamp_utils

#Create config for mathplotlib rc params
rc = {'lines.linewidth': 2, 'axes.labelsize': 18, 'axes.titlesize': 18}
sns.set(rc=rc)

#Load in the data
bd_1975 = np.loadtxt('data/beak_depth_scandens_1975.csv')
bd_2012 = np.loadtxt('data/beak_depth_scandens_2012.csv')

#Plot the ecdf to see what the data looks like
x_1975, y_1975 = bootcamp_utils.ecdf(bd_1975)
x_2012, y_2012 = bootcamp_utils.ecdf(bd_2012)

#Generate bootstrap sample
#random.choice is choosing random numbers from within bd_1975 without choosing the same numbers again
bs_sample_1975 = np.random.choice(bd_1975, replace=True, size=len(bd_1975))
bs_sample_2012 = np.random.choice(bd_2012, replace=True, size=len(bd_2012))

#Replicate of the mean
#bs_replicate = np.mean(bs_sample)

#Generate lots of replicates ; Bootstrap replicates
n_reps= 10000 #Number of replicates
bs_replicates_1975 = np.empty(n_reps)
for i in range(n_reps):
    bs_sample = np.random.choice(bd_1975, replace=True, size=len(bd_1975))
    bs_replicates_1975[i] = np.mean(bs_sample)

conf_int_1975 = np.percentile(bs_replicates_1975, [2.5, 97.5])

bs_replicates_2012 = np.empty(n_reps)
for i in range(n_reps):
    bs_sample = np.random.choice(bd_2012, replace=True, size=len(bd_2012))
    bs_replicates_2012[i] = np.mean(bs_sample)

conf_int_2012 = np.percentile(bs_replicates_1975, [2.5, 97.5])

print(conf_int_1975, conf_int_2012)

#Can change the above of np.mean to np.std

#x_1975_bs, y_1975_bs = bootcamp_utils.ecdf(bd_1975)
#x_2012_bs, y_2012_bs = bootcamp_utils.ecdf(bd_2012)

# plt.close()
# plt.plot(x_1975, y_1975, marker='^',linestyle='none', alpha=0.5)
# plt.plot(x_2012, y_2012, marker='^',linestyle='none', alpha=0.5)
# plt.plot(x_1975_bs, y_1975_bs, marker='v',linestyle='none')
# plt.plot(x_2012_bs, y_2012_bs, marker='v',linestyle='none')
# plt.xlabel('beak depth (mm)')
# plt.ylabel('ECDF')
# plt.legend(('1975', '2012', '1975 bs', '2012 bs'), loc="lower right")
# plt.margins(0.02)
# plt.show()

#Histogram of the mean from the bs replicates for 1975
#plt.hist(bs_replicates_1975, bins=100)
#plt.show()

#Confidence interval
# conf_interval = np.percentile(bs_replicates_1975, [2.5, 97.5])
# print(conf_interval)

#Compute the mean beak depth
print('Mean: 1975 is', np.mean(bd_1975), '2012 is', np.mean(bd_2012))

#What is the sample size?
print('Sample Size: 1975 is ', len(bd_1975), '2012 is', len(bd_2012))


#Confidence interval
#95% confidence interval
#What happens if you repeat an experiment over and over again,
#95% of the times is that the observed data will be between the mean
#Has nothing to do with the true value of the experiment
#With the computer you can simulate the experiment over and over

#bootstrap method
#Why does bootstrap work? Brad Efron
