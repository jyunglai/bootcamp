import numpy as np
import scipy.special
import matplotlib.pyplot as plt
import seaborn as sns

#Generate an array of x values
x = np.linspace(-15, 15, 400) #From -15 to 15 and 400 values

#Compute the normalized intensity
norm_I = 4 * (scipy.special.j1(x) / x)**2

#Plot our computation
plt.close()
plt.plot(x, norm_I, marker='.', linestyle='none')
plt.xlabel('$x$') #Display in mathematical text
plt.margins(0.02) #Expand by a factor of 2%
plt.ylabel('$I(x) / I_0$')
#plt.show()

#Processing the spike data
data = np.loadtxt('data/retina_spikes.csv', skiprows=2, delimiter=',')
t = data[:,0] #Everything in the first column
V = data[:,1] #Take everything in the second column

#Close all other plots
plt.close()

plt.plot(t,V)
plt.xlabel('t (ms)')
plt.ylabel('v (µV)')
plt.xlim(1395, 1400) #Looking at a 500 range of x
plt.show()
