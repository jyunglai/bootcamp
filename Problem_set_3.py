import numpy as np
import scipy.special
import matplotlib.pyplot as plt
import seaborn as sns

rc={'lines.linewidth': 2, 'axes.labelsize': 18, 'axes.titlesize': 18}
sns.set(rc=rc)

# The following is specific Jupyter notebooks
#%matplotlib inline
#%config InlineBackend.figure_formats = {'png', 'retina'}

#Problem 3:2 Data Collapse
#Part a - Load 3 data sets
wt_lac = np.loadtxt('data/wt_lac.csv', delimiter=',', skiprows=3)
q18m_lac = np.loadtxt('data/q18m_lac.csv', delimiter=',', skiprows=3)
q18a_lac = np.loadtxt('data/q18a_lac.csv', delimiter=',', skiprows=3)

wt_lac_iptg = wt_lac[:,0]
wt_lac_fold_change = wt_lac[:,1]

q18a_lac_iptg = q18a_lac[:,0]
q18a_lac_fold_change = q18a_lac[:,1]

q18m_lac_iptg = q18m_lac[:,0]
q18m_lac_fold_change = q18m_lac[:,1]

plt.loglog(wt_lac_iptg, wt_lac_fold_change, marker='.', linestyle='none', markersize=20, alpha=0.5)
plt.plot(q18a_lac_iptg, q18a_lac_fold_change, marker='.', linestyle='none', markersize=20, alpha=0.5)
plt.plot(q18m_lac_iptg, q18m_lac_fold_change, marker='.', linestyle='none', markersize=20, alpha=0.5)

plt.margins(0.03)
plt.xlabel('IPTG(µm)')
plt.ylabel('Fold Change')
plt.legend(('wt-lac', 'q18a-lac', 'q18m-lac'), loc='lower right')
plt.show()
