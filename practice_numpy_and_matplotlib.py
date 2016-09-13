import numpy as np
import scipy.stats
import matplotlib.pyplot as plt
import seaborn as sns

#Create config for mathplotlib rc params
rc = {'lines.linewidth': 2, 'axes.labelsize': 18, 'axes.titlesize': 18}
sns.set(rc=rc)

#Load text
data_txt = np.loadtxt('data/collins_switch.csv', delimiter=',', skiprows=2)

# #Slice out iptg and gfp
# iptg = data_txt[:,0] #First column
# gfp = data_txt[:,1] #Second column
#
# #plot iptg and gfp
# plt.close()
# plt.semilogx(iptg, gfp, linestyle='none', marker='.', markersize=20)
# plt.xlabel('IPTG (mM)')
# plt.ylabel('Normalized GFP')
# plt.title('IPTG Titration - Semilogx')
# plt.ylim(-0.02, 1.02)
# plt.xlim(8e-4, 15)
# plt.show()

#plot iptg and gfp
# plt.close()
# plt.loglog(iptg, gfp, linestyle='none', marker='.', markersize=20)
# plt.xlabel('IPTG (mM)')
# plt.ylabel('Normalized GFP')
# plt.title('IPTG Titration - Log - log')
# plt.ylim(-0.02, 1.02)
# plt.xlim(8e-4, 15)
# plt.show()

#Slice out iptg and gfp
iptg = data_txt[:,0] #First column
gfp = data_txt[:,1] #Second column
sem = data_txt[:,2] #Third column


#plot iptg and gfp
# plt.close()
# plt.errorbar(iptg, gfp, yerr=sem, linestyle='none', marker='.', markersize=20)
# plt.xlabel('IPTG (mM)')
# plt.ylabel('Normalized GFP')
# plt.title('IPTG Titration - semilog X w/ Error Bar')
# plt.ylim(-0.02, 1.02)
# plt.xlim(8e-4, 15)
# plt.xscale('log')
# plt.show()

#Pratice exercise 3
