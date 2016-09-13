import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#Create config for mathplotlib rc params
rc = {'lines.linewidth': 2, 'axes.labelsize': 18, 'axes.titlesize': 18}
sns.set(rc=rc)

#Load the food data
xa_high = np.loadtxt('data/xa_high_food.csv', comments = '#')
xa_low = np.loadtxt('data/xa_low_food.csv', comments = '#')

#Specify range of values that each bin represents
#Make the bin boundars
low_min = np.min(xa_low)
low_max = np.max(xa_low)
high_min = np.min(xa_high)
high_max = np.min(xa_low)
global_min = np.min([low_min, high_min])
global_max = np.max([low_max, high_max])

bins = np.arange(global_min-50, global_max+50, 50) #Every 50 will make a bin from 1700 to 2500

#Plot the data as histogram
#_ = plt.hist((xa_low, xa_high), bins=bins) #_ is a garbage collector
#plt.xlabel('Cross-secional area (µm$^2$)')
#plt.ylabel('Count')
#plt.show()

#Plot data as 2 overlaid histograms
_ = plt.hist(xa_low, normed=True, bins=bins, histtype='stepfilled', alpha=0.5)
_ = plt.hist(xa_high, normed=True, bins=bins, histtype='stepfilled', alpha=0.5)
plt.xlabel('Cross-secional area (µm$^2$)')
plt.ylabel('Frequency')
plt.legend(('low concentration', 'high concentration'), loc='upper right')
plt.show()

#Saving the figure
#plt.savefig('egg_area_histograms.svg', bbox_inches='tight')
plt.savefig('egg_area_histograms.pdf', bbox_inches='tight')
