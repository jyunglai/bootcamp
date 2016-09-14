import numpy as np
import bootcamp_utils
import matplotlib.pyplot as plt
import seaborn as sns

#Create config for mathplotlib rc params
rc = {'lines.linewidth': 2, 'axes.labelsize': 18, 'axes.titlesize': 18}
sns.set(rc=rc)

#Random number between 0 and 1
print(np.random.random()) #Mercet Twister algorithm

# np.random.seed(42)
# print(np.random.random())

#How to test if the numbers are random
#Plot a histogram, plot the ecdf to see if it's random

#x = np.random.random(size=100000)

#x_ecdf, y_ecdf = bootcamp_utils.ecdf(x)

#x_ecdf[]::1000] #Select every 1000th point from array
#Plot ecdf lines from random number generation
# plt.close()
# plt.plot(x_ecdf[::1000], y_ecdf[::1000], marker='.', linestyle='none', markersize=10)
# plt.show()

#How to flip a coin with random number generator
x = np.random.random(size=36)
heads = x <= 0.5 #Checks every numpy array and returns an array that shows if it's heads or tails
print(heads)

#sum gets the number of heads
print(np.sum(heads))
#This allows you to get a distribution that checks how random your results are

#Getting numbers out closer to the mean of a set of numbers
p = np.random.normal(7, 1, size=10)
print(p)

# p2 = np.random.normal(7, 1, size=10000)
#
# plt.close()
# plt.hist(p2, bins=100, alpha=0.8)
# plt.margins(0.02)
# plt.show()

#Drawing numbers 0, 1, 2, and 3
p3 = np.random.randint(0, 4, size = 20)
print(p3)

#How is this useful?
#Random nucleotides
base = 'ATGC'
randomBases = np.random.randint(0, 4, size = 50)

seq_list = [None]*50
for i, b in enumerate(randomBases):
    seq_list[i] = base[b]

print(seq_list)

print(''.join(seq_list)) #Creates the random DNA sequences

#96 well plate and send 20 samples from them
np.random.randint(0, 96, 20)

#Problem: There is a repeat.  Can have an option to choose a replacement or nucleotides
p4 = np.random.choice(np.arange(96), size=20, replace=False)
print(p4)

#Random deck of cards
p5 = np.random.permutation(np.arange(52))
print(p5)
