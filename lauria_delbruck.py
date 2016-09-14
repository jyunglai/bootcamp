import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import bootcamp_utils

#Create config for mathplotlib rc params
rc = {'lines.linewidth': 2, 'axes.labelsize': 18, 'axes.titlesize': 18}
sns.set(rc=rc)

#Specify parameters
#number of generations
n_gen = 16

#Chance of having beneficial mutation
r = 1e-5

#Total number of cells (Exponentional growth)
n_cells = 2**(n_gen-1)

#Adaptive Immunity hypothesis
#Take out of binomial random distribution
ai_samples = np.random.binomial(n_cells, r, size=10000)

#Report mean and std
print("AI mean: ", np.mean(ai_samples))
print("AI std: ", np.std(ai_samples))
print("AI Fano: ", np.var(ai_samples) / np.mean(ai_samples))

#Function to draw out of random mutation hypothesis
#Number of cells that can get the mutation = 2 * (2**g-1 - n_mut)
#This assumes that there is only one mutation and no other mutations are lost or gained
def draw_random_mutation(n_gen, r):
    """
    Draw sample under random mutation hypothesis
    """
    #Initialize number of mutations
    n_mut = 0

    for g in range(n_gen):
        n_mut = 2*n_mut + np.random.binomial(2**g - 2*n_mut, r)

    return n_mut

def sample_random_mutation(n_gen, r, size=1):
    #initialize samples
    samples = np.empty(size)

    #Draw the samples
    for i in range(size):
        samples[i] = draw_random_mutation(n_gen, r)

    return samples

rm_samples = sample_random_mutation(n_gen, r, size=100000)

x_ai, y_ai = bootcamp_utils.ecdf(ai_samples)
x_rm, y_rm = bootcamp_utils.ecdf(rm_samples)

plt.plot(x_ai, y_ai, marker='.', linestyle='none')
plt.plot(x_rm, y_rm, marker='.', linestyle='none')
plt.xscale('log')
plt.margins(0.02)
plt.show()

print("RM mean: ", np.mean(rm_samples))
print("RM std: ", np.std(rm_samples))
print("RM Fano: ", np.var(rm_samples) / np.mean(rm_samples))

#Plot
# counts = np.bincount(ai_samples) #Counts the number of the same samples
# plt.plot(np.arange(len(counts)), counts, marker='.', linestyle='none')
# plt.show()
