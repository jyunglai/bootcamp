import numpy as np

xa_high = np.loadtxt('data/xa_high_food.csv')
xa_low = np.loadtxt('data/xa_low_food.csv')

xa_high_mean = np.mean(xa_high)
xa_high_std = np.std(xa_high)

xa_low_mean = np.mean(xa_low)
xa_low_std = np.std(xa_low)

print("""For high concentration mean egg size is {0:f} +/- {1:f}
For low Concentration, mean egg size is {2:f} +/- {3:f}""".format(xa_high_mean, xa_high_std, xa_low_mean, xa_low_std))

high_perc = np.percentile(xa_high, (25, 50, 75))
low_perc = np.percentile(xa_low, (25, 50, 75))

print("""For high, percentiles are {0:d}, {1:d}, {2:d}.
For low, percentiles are {3:d}, {4:d}, {5:d}."""),
format(*(tuple(high_perc.astype(int)), tuple(low_perc.astype(int)))))
