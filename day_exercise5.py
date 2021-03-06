import numpy as np
import scipy.stats
import matplotlib.pyplot as plt
import seaborn as sns
import bootcamp_utils

#Create config for mathplotlib rc params
rc = {'lines.linewidth': 2, 'axes.labelsize': 18, 'axes.titlesize': 18}
sns.set(rc=rc)

#Load text
xa_high = np.loadtxt('data/xa_high_food.csv', comments = '#')
xa_low = np.loadtxt('data/xa_low_food.csv', comments = '#')

x = np.linspace(1600, 2500, 400)
#Generate guassian cdf
cdf_high = scipy.stats.norm.cdf(x, loc=np.mean(xa_high), scale=np.std(xa_high))
cdf_low = scipy.stats.norm.cdf(x, loc=np.mean(xa_low), scale=np.std(xa_low))

x_high, y_high = bootcamp_utils.ecdf(xa_high)
x_low, y_low = bootcamp_utils.ecdf(xa_low)
plt.close()
plt.plot(x_high, y_high, marker='.', linestyle='none', markersize=20, alpha=0.5)
plt.plot(x_low, y_low, marker='.', linestyle='none', markersize=20, alpha=0.5)

#Plot cdf
plt.plot(x, cdf_high, color='gray')
plt.plot(x, cdf_low, color='gray')

plt.margins(0.03)
plt.xlabel('Cross-sectional area (µm)')
plt.ylabel('eCDF')
plt.legend(('high food', 'low food'), loc='lower right')
plt.show()
